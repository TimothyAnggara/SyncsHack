import React from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js/auto";

function LineChart({passedData, timeframe}) {
  // console.log(passedData)
  console.log(passedData.daily["Time Series (Daily)"])
  console.log(passedData.weekly["Weekly Adjusted Time Series"])
  console.log(passedData.monthly["Monthly Adjusted Time Series"])
  let selectedData;
  switch (timeframe) {
    case 'daily':
      selectedData = passedData.daily["Time Series (Daily)"];
      break;
    case 'weekly':
      selectedData = passedData.weekly["Weekly Adjusted Time Series"];
      break;
    case 'monthly':
      selectedData = passedData.monthly["Monthly Adjusted Time Series"];
      break;
    default:
      selectedData = passedData.daily["Time Series (Daily)"]; // Default to daily if no match
  }
  
  // console.log(timeframe)
  // console.log(selectedData)
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
      }
    ]
  };
  
  return <Line data={chartData} />;
}

export default LineChart;