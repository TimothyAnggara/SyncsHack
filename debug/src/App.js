import { useState } from "react";
import "./App.css";
import LineChart from "./Component/LineChart";
import axios from "axios";

function App() {
  const handleChange = (e) =>{
    setTicker(e.target.value);
  }
  const [ticker, setTicker] = useState("");
  const [defaultData, setDefaultData] = useState(null);
  const [displayedTicker, setDisplayedTicker] = useState("");
  const [chartData, setChartData] = useState(null)
  const [timeframe, setTimeFrame] = useState("Daily");
 
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      setDisplayedTicker(ticker);
      axios.get(`http://localhost:5000/fetchData/${ticker}`)
      .then(response => {
        // process the response data (you might want to update your state with this data)
        setDefaultData(response.data)

      }).catch(error => {
        console.error("Error fetching data: ", error)
      })
    }
  }
  const selectTimeFrame = (frame) => {
    setTimeFrame(frame);
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
      <div className="selectors-containers">
      <button 
        className={timeframe === "Daily" ? "selected" : ""} 
        onClick={() => selectTimeFrame("Daily")}>
        Daily
      </button>
      <button 
        className={timeframe === "Weekly" ? "selected" : ""} 
        onClick={() => selectTimeFrame("Weekly")}>
        Weekly
      </button>
      <button 
        className={timeframe === "Monthly" ? "selected" : ""} 
        onClick={() => selectTimeFrame("Monthly")}>
        Monthly
      </button>
      </div>
      <div className="chart-container" >
        {displayedTicker && <h1 className="ticker-heading">{displayedTicker}</h1>}
        <LineChart chartData = {defaultData} timeframe={timeframe}/>
      </div>
    </div>
  )
}

export default App;
