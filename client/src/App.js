import './App.css';
import React, { useState } from 'react';

function App() {
  const [question, setQuestion] = useState("what is the problem with the drivers ?");
  const [context, setContext] = useState("The interface of the app is good and very easy to navigate. Only problem is the drivers cancels the ride 8 out of 10 times I've used Uber. It is really frustrating when you are in a hurry. I think some actions should be put forward for the drivers as well to not cancel the request once accepted. In few instances, despite the driver canceling the ride, I had to pay the penalty fee. What I wrote is an honest opinion, after using Uber to book a ride for several months now.");
  const [answer, setAnswer] = useState([]);


  
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
      setAnswer(data)
    })
  };

  function AnswersList() {
    return (
      <>
        <p className='label_text'>Answer List</p>
        <br/>
        <br/>
        <br/>
        <div className='input_answer_full'>
        <ul className='input_answer'>  
        {answer.map((item) => ( <li key={item["answer"]}>{item["answer"]}</li>))}
        </ul>
        <ul className='input_answer_score'>  
        {answer.map((item) => ( <li key={item["answer"]}>{item["score"]} &emsp; {item["cossine_sim"]} &emsp; {item["score_final"]}</li>))}
        </ul>
        </div>
      </>
    );
  }

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
      <AnswersList />
    </div>
  );
}

export default App;
