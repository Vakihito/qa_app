import './App.css';
import React, { useState } from 'react';

function App() {
  const [question, setQuestion] = useState("why I'm sad ?");
  const [context, setContext] = useState("I'm sad because I have too much work");
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
        <label>
          Enter your Context : 
          <input type="text" value={context} onChange={(e) => setContext(e.target.value)} />
        </label>
        <br />
        <br />
        <label>
          Enter your Question : 
          <input type="text" value={question} onChange={(e) => setQuestion(e.target.value)} />
        </label>
        <br />
        <br />
        <input type="submit" value="Submit" />
      </form>
      <h1>Answer: {answer}</h1>
      <h2>Score: {prob}</h2>
    </div>
  );
}

export default App;
