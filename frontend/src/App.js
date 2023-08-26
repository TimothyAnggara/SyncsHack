import { useState } from 'react';
import './App.css';
import React from 'react';
import Searchbar from './Components/LineChart';



function App() {
  const [ticker , setTicker] = useState("")
  const searchClicked = (value) => {
    setTicker(value)
  }
  // Handler to update the state when the input value changes
  const handleInputChange = (e) => {
    setTicker(e.target.value);
  };

  // Handler for the form submission
  const handleSubmit = (e) => {
      e.preventDefault();
      console.log('Stock Ticker:', ticker);
      // Here, you can do whatever you want with the ticker value, e.g., fetch data or update other states
  } 
  
  return (
   <div className = "app">
    <Searchbar />
    {/* <LineChart /> */}

    </div>
  );
}

export default App;
