import './App.css';
import React, { useState } from 'react';

function App() {
  const [question, setQuestion] = useState("why I'm sad ?");
  const [context, setContext] = useState("I'm sad because I have to work with frontend ...");
  const [answer, setAnswer] = useState('');
  const [prob, setProb] = useState('');


  
  const handleSubmit = (event) => {
    event.preventDefault();
    fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      body: JSON.stringify({
        context: context,
        question : question
      })
    })
    .then(response => response.json())
    .then(data => {
      setAnswer(data['answer'])
      setProb(data['score'])
    })
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label className='label_text'>
          Enter your Context
        </label>
        <br />
        <br />
        <textarea className='input_context' type="text" value={context} onChange={(e) => setContext(e.target.value)} />
        <br />
        <br />
        <label className='label_text'>
          Enter your Question
        </label>
        <br />
        <br />
        <textarea className='input_question' type="text" value={question} onChange={(e) => setQuestion(e.target.value)} />
        <br />
        <br />
        <input type="submit" value="Submit" />
      </form>
      <p className='label_text' >Predicted Answer</p>
      <br />
      <p className='input_answer' >{answer}</p>
      <br />
      <p>Score: {prob}</p>
    </div>
  );
}

export default App;
