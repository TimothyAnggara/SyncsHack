import { useState, useEffect } from "react";
import "./App.css";
import LineChart from "./Component/LineChart";
import axios from "axios";
import sampledata from "./data.json"

function App() {
  const handleChange = (e) =>{
    setTicker(e.target.value);
  }
  const [ticker, setTicker] = useState("");
  const [defaultData, setDefaultData] = useState(sampledata);
  const [displayedTicker, setDisplayedTicker] = useState("");
  const [chartData, setChartData] = useState(null)
  const [timeframe, setTimeFrame] = useState("Daily");
 
  //Handles the logic if the users presses enter after typing the ticker
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      setDisplayedTicker(ticker);
      axios.get(`http://localhost:5000/fetchData/${ticker}`)
      .then(response => {
        // process the response data (you might want to update your state with this data)
        setDefaultData(response.data)
        console.log(defaultData)
      }).catch(error => {
        console.error("Error fetching data: ", error)
      })
    }
  }
  // Handles the logic of clicking the timeframe buttons
  const selectTimeFrame = (frame) => {
    setTimeFrame(frame);
    console.log(frame)
  }

  // Handles the logic if the user clicks on the search button
  const handleSearchClick = () => {
    setDisplayedTicker(ticker);
    axios.get(`http://localhost:5000/fetchData/${ticker}`)
      .then(response => {
        // process the response data (you might want to update your state with this data)
        setDefaultData(response.data)
        console.log(defaultData)
      }).catch(error => {
        console.error("Error fetching data: ", error)
      })
  }

  // useEffect(() => {
  //   console.log('Timeframe has changed:', timeframe);
  // }, [timeframe]);  // This dependency array ensures the effect runs only when `timeframe` changes

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
        onClick={() => selectTimeFrame("daily")}>
        Daily
      </button>
      <button 
        className={timeframe === "Weekly" ? "selected" : ""} 
        onClick={() => selectTimeFrame("weekly")}>
        Weekly
      </button>
      <button 
        className={timeframe === "Monthly" ? "selected" : ""} 
        onClick={() => selectTimeFrame("monthly")}>
        Monthly
      </button>
      </div>
      <div className="chart-container" >
        {displayedTicker && <h1 className="ticker-heading">{displayedTicker}</h1>}
        <LineChart key={timeframe} passedData = {defaultData} timeframe={timeframe}/>
      </div>
    </div>
  )
}

export default App;
