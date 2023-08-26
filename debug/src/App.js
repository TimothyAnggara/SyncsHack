import { useState } from "react";
import "./App.css";
import LineChart from "./Component/LineChart";

function App() {
  const handleChange = (e) =>{
    setTicker(e.target.value);
  }
  const [ticker, setTicker] = useState("")
  const [displayedTicker, setDisplayedTicker] = useState("");
 
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      setDisplayedTicker(ticker);
    }
  }
  
  const handleSearchClick = () => {
    setDisplayedTicker(ticker);
}
  return(
    <div className="app">
      <div className="search-container">
      <input 
        type = "text"
        placeholder = "input ticker"
        onChange = {handleChange}
        onKeyDown={handleKeyDown}
        value = {ticker}/>
        <button className="search-button" onClick={handleSearchClick}>
          <img src="/Images/search-icon.svg" alt="search-icon"/>
        </button>
      </div>
      <div className="chart-container" >
        {displayedTicker && <h1 className="ticker-heading">{displayedTicker}</h1>}
        <LineChart />
      </div>
    </div>
  )
}

export default App;
