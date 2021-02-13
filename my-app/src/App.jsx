import React, { useState } from 'react';
import './App.css';

function App() {
  const [moveToTake, setMoveToTake] = useState('');
  const [positions, setPositions] = useState([]);

  async function handleClick() {
    if (positions.length > 0) {
      try {
        const requestData = {
          method: 'post',
          headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ test: positions })
        };
  
        const response = await fetch(
          'http://localhost:5000/get-best-move',
          requestData
        );
        const data = await response.json();
  
        setMoveToTake(data);
      } catch (err) {
        console.log(err);
      }
    }
  }

  return (
    <div className="App">
      <h1>Grundy's game - next move picker</h1>
      <p>Hello there mate, lets figure out your best move!</p>

      <p>This assumes it is now your turn, and, we are trying to help you win the game.</p>
      <div className="input-container">
        <label htmlFor="positions">Enter current coin positions: </label>
        <input
          name="positions"
          type="text"
          onChange={(e) => setPositions(e.target.value)}
          placeholder="e.g. 3,1,1,2"
        ></input>
      </div>
      <button onClick={handleClick}>Get your best move</button>
      { moveToTake.length > 0 && (<p>your best move is: {moveToTake}</p>)}
    </div>
  );
}

export default App;
