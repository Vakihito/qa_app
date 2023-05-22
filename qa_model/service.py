import numpy as np
import bentoml
from bentoml.io import JSON
from math import ceil
from transformers import AutoTokenizer
from transformers import AutoModelForQuestionAnswering
from transformers import pipeline

MODEL_PATH = "model"

class TransformerPipelineRunner(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu")
    SUPPORTS_CPU_MULTI_THREADING = True

    def __init__(self):
        
        self.model = AutoModelForQuestionAnswering.from_pretrained(MODEL_PATH) # loading the model
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)                # loading the tokenizer
        self.question_answerer = pipeline("question-answering", model=self.model, tokenizer=self.tokenizer)


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
            return [answers]  
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
