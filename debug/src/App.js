import { useState, useEffect } from "react";
import "./App.css";
import LineChart from "./Component/LineChart";
import axios from "axios";
import sampledata from "./data.json"
import rsi_sample_data from "./rsi-close.json"
import sma_sample_data from "./sma-close.json"
import ema_sample_data from "./ema-close.json"

function App() {
  const handleChange = (e) =>{
    setTicker(e.target.value);
  }
  const [ticker, setTicker] = useState("");
  const [defaultData, setDefaultData] = useState(sampledata);
  const [displayedTicker, setDisplayedTicker] = useState("");
  const [chartData, setChartData] = useState(null)
  const [timeframe, setTimeFrame] = useState("Daily");
  const [rsi, setRsi] = useState(rsi_sample_data)
  const [sma, setSma] = useState(sma_sample_data)
  const [ema, setEma] = useState(ema_sample_data);
 
  //Handles the logic if the users presses enter after typing the ticker
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      setDisplayedTicker(ticker);
      axios.get(`http://localhost:5000/fetchData/${ticker}`)
      .then(response => {
        // process the response data (you might want to update your state with this data)
        setDefaultData(response.data)
        console.log(defaultData)
      }).then(response => {
        // process the response data (you might want to update your state with this data)
        fetchRSIData()
        fetchSMAData()
        fetchEMAData()
      }).catch(error => {
        console.error("Error fetching data: ", error)
      })
    }
  }
  // Handles the logic of clicking the timeframe buttons
  const selectTimeFrame = (frame) => {
    setTimeFrame(frame);
  }

  // Handles the logic if the user clicks on the search button
  const handleSearchClick = () => {
    setDisplayedTicker(ticker);
    axios.get(`http://localhost:5000/fetchData/${ticker}`)
      .then(response => {
        // process the response data (you might want to update your state with this data)
        setDefaultData(response.data)
      }).then(response => {
        // process the response data (you might want to update your state with this data)
        fetchRSIData()
        fetchSMAData()
        fetchEMAData()
      }).then(response => {
        // process the response data (you might want to update your state with this data)
        console.log("HEGOAJSPIASGAG")
        console.log(rsi)
        console.log("HEGOAJSPIASGAG")
        console.log(sma)
        console.log("HEGOAJSPIASGAG")
        console.log(ema)
      }).catch(error => {
        console.error("Error fetching data: ", error)
      })
  }

  const fetchSMAData = () => {
    axios.get('http://localhost:5000/sma')
        .then(response => {
            console.log('SMA Data:', response.data);
            // You can set this data to a state variable or process it further as required
            setSma(response.data);
        })
        .catch(error => {
            console.error('Error fetching SMA data:', error);
        });
  };

  const fetchRSIData = () => {
    axios.get('http://localhost:5000/rsi')
        .then(response => {
            console.log('RSI Data:', response.data);
            // You can set this data to a state variable or process it further as required
            setRsi(response.data);
        })
        .catch(error => {
            console.error('Error fetching RSI data:', error);
        });
    };

    const fetchEMAData = () => {
      axios.get('http://localhost:5000/ema')
          .then(response => {
              console.log('EMA Data:', response.data);
              // You can set this data to a state variable or process it further as required
              setEma(response.data);
          })
          .catch(error => {
              console.error('Error fetching EMA data:', error);
          });
      };

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
        <LineChart key={timeframe} passedData = {defaultData} smaData = {sma} rsiData = {rsi} emaData = {ema} timeframe={timeframe}/>
      </div>
    </div>
  )
}

export default App;
