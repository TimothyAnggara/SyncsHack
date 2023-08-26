import { useState } from 'react';
import './App.css';
import { Button, Input } from 'antd';


function App() {
  const [ticker , setTicker] = useState("")

  const buttonClicked = () =>{
    console.log(ticker)
  }
  return (
    <div className="App">
      <Input
        placeholder="Enter text here"
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
      enterButton/> 
      <Button onClick={buttonClicked}/>
    </div>
  );
}

export default App;
