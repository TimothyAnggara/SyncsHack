import React from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js/auto";

function LineChart({passedData, rsiData, emaData, timeframe}) {
  let selectedData;
  let selectedEma;
  let selectedRsi;
  console.log(emaData)
  switch (timeframe) {
    case 'daily':
      selectedData = passedData.daily["Time Series (Daily)"];
      selectedEma = emaData.daily
      selectedRsi = rsiData.daily
      break;
    case 'weekly':
      selectedData = passedData.weekly["Weekly Adjusted Time Series"];
      selectedEma = emaData.weekly
      selectedRsi = rsiData.weekly
      break;
    case 'monthly':
      selectedData = passedData.monthly["Monthly Adjusted Time Series"];
      selectedEma = emaData.monthly
      selectedRsi = rsiData.monthly
      break;
    default:
      selectedData = passedData.daily["Time Series (Daily)"]; // Default to daily if no match
      selectedEma = emaData.daily
      selectedRsi = rsiData.monthly
    }


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