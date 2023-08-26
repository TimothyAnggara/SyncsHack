import { useState } from "react";
import "./App.css";
import LineChart from "./Component/LineChart";
import { UserData } from "./Data";

function App() {
  const handleChange = (e) =>{
    setTicker(e.target.value);
  }
  const [ticker, setTicker] = useState("")
  const [displayedTicker, setDisplayedTicker] = useState("");
  const [userData, setUserData] = useState({
    labels: UserData.map((data) => data.year),
    datasets: [
      {
        label: "Users Gained",
        data: UserData.map((data) => data.userGain),
        backgroundColor: [
          "rgba(75,192,192,1)",
          "#ecf0f1",
          "#50AF95",
          "#f3ba2f",
          "#2a71d0",
        ],
        borderColor: "black",
        borderWidth: 2,
      },
    ],
  });
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      setDisplayedTicker(ticker);
    }
  }
  
  const handleSearchClick = () => {
    // Set the displayedTicker to the current ticker value
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
        <LineChart chartData={userData} />
      </div>
    </div>
  )
}

export default App;
