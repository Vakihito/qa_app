import numpy as np
import bentoml
from bentoml.io import JSON
from math import ceil
from transformers import AutoTokenizer
from transformers import AutoModelForQuestionAnswering
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from numpy.linalg import norm

MODEL_PATH = "model"

class TransformerPipelineRunner(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu")
    SUPPORTS_CPU_MULTI_THREADING = True

    def __init__(self):
        
        self.model = AutoModelForQuestionAnswering.from_pretrained(MODEL_PATH) # loading the model
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)                # loading the tokenizer
        self.question_answerer = pipeline("question-answering", model=self.model, tokenizer=self.tokenizer)
        self.encoder = SentenceTransformer("multi-qa-mpnet-base-dot-v1", device='cuda')


    @bentoml.Runnable.method(batchable=False, batch_dim=0)
    def predict(self, input):
        contexts = input['context'].split('.')
        questions = []
        print(f"contexts {contexts}")
        print(f"questions {questions}")
        list_contexts = []
        for cur_context in contexts:
            if len(cur_context) > 0:
                list_contexts.append(cur_context)
                questions.append(input['question'])
        
        answers = self.question_answerer(question=questions, context=list_contexts)
        print(f"[INFO] possible answers {answers}")
        
        if isinstance(answers, dict):
            answers = [answers]  
        
        print("encoding the data")
        
        only_answer_text = [cur_ans['answer'] for cur_ans in answers]
        encoded_question = np.array(self.encoder.encode(questions, device='cpu'))
        encoded_answers = np.array(self.encoder.encode(only_answer_text, device='cpu'))
        
        encoded_question_norm = norm(encoded_question)
        encoded_answers_norm = norm(encoded_answers, axis=1)
        cossine_preds = np.sum(encoded_answers * encoded_question, axis=1) / (encoded_question_norm * encoded_answers_norm)
        
        for cur_ans, conssine_preds in zip(answers, cossine_preds):
            cur_ans["cossine_sim"] = conssine_preds
        
        return answers
        
model_runner = bentoml.Runner(TransformerPipelineRunner)
svc = bentoml.Service("deberta_qa_model", runners=[model_runner])


@svc.api(input=JSON(), output=JSON())
def predict(input):
    """"""
    print(f"[INPUT] {input}")
    
    
    predictions = model_runner.predict.run(input)
    
    print(f"[RESPONSE] {predictions}")
    
    return predictions
