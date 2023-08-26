import React from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js/auto";

function LineChart({passedData, rsiData, emaData, smaData, timeframe}) {
  let selectedData;
  let selectedEma;
  let selectedRsi;
  let selectedSma;
  console.log({name:"Passed Data", passedData})
  console.log({name:"RSI", emaData})
  console.log({name:"SMA", smaData})
  console.log({name:"EMA", emaData})
  switch (timeframe) {
    case 'daily':
      selectedData = passedData['daily']["Time Series (Daily)"];
      selectedEma = Object.values(emaData.Daily)
      selectedRsi = Object.values(rsiData.Daily)
      selectedSma = Object.values(smaData.Daily)
      break;
    case 'weekly':
      selectedData = passedData['weekly']["Weekly Adjusted Time Series"];
      selectedEma = Object.values(emaData.Weekly)
      selectedRsi = Object.values(rsiData.Weekly)
      selectedSma = Object.values(smaData.Weekly)
      break;
    case 'monthly':
      selectedData = passedData['monthly']["Monthly Adjusted Time Series"];
      selectedEma = Object.values(emaData.Monthly)
      selectedRsi = Object.values(rsiData.Monthly)
      selectedSma = Object.values(smaData.Monthly)
      break;
    default:
      selectedData = passedData['daily']["Time Series (Daily)"]; // Default to daily if no match
      selectedEma = Object.values(emaData.Daily)
      selectedRsi = Object.values(rsiData.Daily)
      selectedSma = Object.values(smaData.Daily)
 
    }

  console.log("FJHOASFJHOIASFIOASFJIASFA")
  console.log(selectedData)
  const dates = Object.keys(selectedData);
  const opens = dates.map(date => parseFloat(selectedData[date]["1. open"]));
  const highs = dates.map(date => parseFloat(selectedData[date]["2. high"]));
  const lows = dates.map(date => parseFloat(selectedData[date]["3. low"]));
  const closes = dates.map(date => parseFloat(selectedData[date]["4. close"]));


  const chartData  = {
    labels: dates,
    datasets: [
      {
        label: 'Open',
        data: opens,
        borderColor: 'rgba(75,192,192,1)',
        fill: false
      },
      {
        label: 'High',
        data: highs,
        borderColor: 'rgba(255,99,132,1)',
        fill: false
      },
      {
        label: 'Low',
        data: lows,
        borderColor: 'rgba(255,205,86,1)',
        fill: false
      },
      {
        label: 'Close',
        data: closes,
        borderColor: 'rgba(54,162,235,1)',
        fill: false
      },
      {
        label: 'EMA',
        data: selectedEma,
        borderColor: 'rgba(54,162,235,1)',
        fill: false
      },
      {
        label: 'SMA',
        data: selectedSma,
        borderColor: 'rgba(54,162,235,1)',
        fill: false
      }
    ]
    
  };
  const rsiChart = {
    labels: dates,
    datasets: [
      {
        label: 'RSI',
        data: selectedRsi,
        borderColor: 'rgba(75,192,192,1)',
        fill: false
      }
    ]
  }
  
  return <div className="LineChart-containers">
      <Line data={chartData} />
      <Line data = {rsiChart} />
    </div>;
}

export default LineChart;