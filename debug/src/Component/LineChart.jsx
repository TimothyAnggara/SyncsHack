import React from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js/auto";

function LineChart() {
  const dataObj = {"Meta Data": {"1. Information": "Daily Prices (open, high, low, close) and Volumes", "2. Symbol": "AAPL", "3. Last Refreshed": "2023-08-25", "4. Output Size": "Compact", "5. Time Zone": "US/Eastern"}, "Time Series (Daily)": {"2023-08-25": {"1. open": "177.3800", "2. high": "179.1500", "3. low": "175.8200", "4. close": "178.6100", "5. volume": "51449594"}, "2023-08-24": {"1. open": "180.6740", "2. high": "181.1040", "3. low": "176.0100", "4. close": "176.3800", "5. volume": "54945798"}, "2023-08-23": {"1. open": "178.5200", "2. high": "181.5500", "3. low": "178.3250", "4. close": "181.1200", "5. volume": "52722752"}, "2023-08-22": {"1. open": "177.0600", "2. high": "177.6800", "3. low": "176.2500", "4. close": "177.2300", "5. volume": "42084245"}, "2023-08-21": {"1. open": "175.0700", "2. high": "176.1300", "3. low": "173.7350", "4. close": "175.8400", "5. volume": "46311879"}, "2023-08-18": {"1. open": "172.3000", "2. high": "175.1000", "3. low": "171.9600", "4. close": "174.4900", "5. volume": "61172150"}, "2023-08-17": {"1. open": "177.1400", "2. high": "177.5054", "3. low": "173.4800", "4. close": "174.0000", "5. volume": "66062882"}, "2023-08-16": {"1. open": "177.1300", "2. high": "178.5400", "3. low": "176.5000", "4. close": "176.5700", "5. volume": "46964857"}, "2023-08-15": {"1. open": "178.8800", "2. high": "179.4800", "3. low": "177.0500", "4. close": "177.4500", "5. volume": "43622593"}, "2023-08-14": {"1. open": "177.9700", "2. high": "179.6900", "3. low": "177.3050", "4. close": "179.4600", "5. volume": "43675627"}, "2023-08-11": {"1. open": "177.3200", "2. high": "178.6200", "3. low": "176.5500", "4. close": "177.7900", "5. volume": "52036672"}, "2023-08-10": {"1. open": "179.4800", "2. high": "180.7500", "3. low": "177.6000", "4. close": "177.9700", "5. volume": "54686851"}, "2023-08-09": {"1. open": "180.8700", "2. high": "180.9300", "3. low": "177.0100", "4. close": "178.1900", "5. volume": "60378492"}, "2023-08-08": {"1. open": "179.6900", "2. high": "180.2700", "3. low": "177.5800", "4. close": "179.8000", "5. volume": "67823003"}, "2023-08-07": {"1. open": "182.1300", "2. high": "183.1300", "3. low": "177.3500", "4. close": "178.8500", "5. volume": "97576069"}, "2023-08-04": {"1. open": "185.5200", "2. high": "187.3800", "3. low": "181.9200", "4. close": "181.9900", "5. volume": "115956841"}, "2023-08-03": {"1. open": "191.5700", "2. high": "192.3700", "3. low": "190.6900", "4. close": "191.1700", "5. volume": "62243282"}, "2023-08-02": {"1. open": "195.0400", "2. high": "195.1800", "3. low": "191.8507", "4. close": "192.5800", "5. volume": "50389327"}, "2023-08-01": {"1. open": "196.2350", "2. high": "196.7300", "3. low": "195.2800", "4. close": "195.6050", "5. volume": "35281426"}, "2023-07-31": {"1. open": "196.0600", "2. high": "196.4900", "3. low": "195.2600", "4. close": "196.4500", "5. volume": "38824113"}, "2023-07-28": {"1. open": "194.6700", "2. high": "196.6260", "3. low": "194.1400", "4. close": "195.8300", "5. volume": "48291443"}, "2023-07-27": {"1. open": "196.0200", "2. high": "197.2000", "3. low": "192.5500", "4. close": "193.2200", "5. volume": "47460180"}, "2023-07-26": {"1. open": "193.6700", "2. high": "195.6400", "3. low": "193.3200", "4. close": "194.5000", "5. volume": "47471868"}, "2023-07-25": {"1. open": "193.3300", "2. high": "194.4400", "3. low": "192.9150", "4. close": "193.6200", "5. volume": "37283201"}, "2023-07-24": {"1. open": "193.4100", "2. high": "194.9100", "3. low": "192.2500", "4. close": "192.7500", "5. volume": "45505097"}, "2023-07-21": {"1. open": "194.1000", "2. high": "194.9700", "3. low": "191.2300", "4. close": "191.9400", "5. volume": "71951683"}, "2023-07-20": {"1. open": "195.0900", "2. high": "196.4700", "3. low": "192.4950", "4. close": "193.1300", "5. volume": "59581196"}, "2023-07-19": {"1. open": "193.1000", "2. high": "198.2300", "3. low": "192.6500", "4. close": "195.1000", "5. volume": "80507323"}, "2023-07-18": {"1. open": "193.3500", "2. high": "194.3300", "3. low": "192.4150", "4. close": "193.7300", "5. volume": "48353774"}, "2023-07-17": {"1. open": "191.9000", "2. high": "194.3200", "3. low": "191.8100", "4. close": "193.9900", "5. volume": "50520159"}, "2023-07-14": {"1. open": "190.2300", "2. high": "191.1799", "3. low": "189.6300", "4. close": "190.6900", "5. volume": "41616242"}, "2023-07-13": {"1. open": "190.5000", "2. high": "191.1900", "3. low": "189.7800", "4. close": "190.5400", "5. volume": "41342338"}, "2023-07-12": {"1. open": "189.6800", "2. high": "191.7000", "3. low": "188.4700", "4. close": "189.7700", "5. volume": "60750248"}, "2023-07-11": {"1. open": "189.1600", "2. high": "189.3000", "3. low": "186.6000", "4. close": "188.0800", "5. volume": "46638119"}, "2023-07-10": {"1. open": "189.2600", "2. high": "189.9900", "3. low": "187.0350", "4. close": "188.6100", "5. volume": "59922163"}, "2023-07-07": {"1. open": "191.4100", "2. high": "192.6700", "3. low": "190.2400", "4. close": "190.6800", "5. volume": "46814998"}, "2023-07-06": {"1. open": "189.8400", "2. high": "192.0200", "3. low": "189.2000", "4. close": "191.8100", "5. volume": "45156009"}, "2023-07-05": {"1. open": "191.5650", "2. high": "192.9800", "3. low": "190.6200", "4. close": "191.3300", "5. volume": "46920261"}, "2023-07-03": {"1. open": "193.7800", "2. high": "193.8800", "3. low": "191.7600", "4. close": "192.4600", "5. volume": "31458198"}, "2023-06-30": {"1. open": "191.6300", "2. high": "194.4800", "3. low": "191.2600", "4. close": "193.9700", "5. volume": "85213216"}, "2023-06-29": {"1. open": "189.0800", "2. high": "190.0700", "3. low": "188.9400", "4. close": "189.5900", "5. volume": "46347308"}, "2023-06-28": {"1. open": "187.9300", "2. high": "189.9000", "3. low": "187.6000", "4. close": "189.2500", "5. volume": "51216801"}, "2023-06-27": {"1. open": "185.8900", "2. high": "188.3900", "3. low": "185.6700", "4. close": "188.0600", "5. volume": "50730846"}, "2023-06-26": {"1. open": "186.8300", "2. high": "188.0500", "3. low": "185.2300", "4. close": "185.2700", "5. volume": "48088661"}, "2023-06-23": {"1. open": "185.5500", "2. high": "187.5600", "3. low": "185.0100", "4. close": "186.6800", "5. volume": "53116996"}, "2023-06-22": {"1. open": "183.7400", "2. high": "187.0450", "3. low": "183.6700", "4. close": "187.0000", "5. volume": "51245327"}, "2023-06-21": {"1. open": "184.9000", "2. high": "185.4100", "3. low": "182.5901", "4. close": "183.9600", "5. volume": "49515697"}, "2023-06-20": {"1. open": "184.4100", "2. high": "186.1000", "3. low": "184.4100", "4. close": "185.0100", "5. volume": "49799092"}, "2023-06-16": {"1. open": "186.7300", "2. high": "186.9900", "3. low": "184.2700", "4. close": "184.9200", "5. volume": "101256225"}, "2023-06-15": {"1. open": "183.9600", "2. high": "186.5200", "3. low": "183.7800", "4. close": "186.0100", "5. volume": "65433166"}, "2023-06-14": {"1. open": "183.3700", "2. high": "184.3900", "3. low": "182.0200", "4. close": "183.9500", "5. volume": "57462882"}, "2023-06-13": {"1. open": "182.8000", "2. high": "184.1500", "3. low": "182.4400", "4. close": "183.3100", "5. volume": "54929129"}, "2023-06-12": {"1. open": "181.2700", "2. high": "183.8900", "3. low": "180.9700", "4. close": "183.7900", "5. volume": "54754995"}, "2023-06-09": {"1. open": "181.5000", "2. high": "182.2300", "3. low": "180.6300", "4. close": "180.9600", "5. volume": "48899973"}, "2023-06-08": {"1. open": "177.8950", "2. high": "180.8400", "3. low": "177.4600", "4. close": "180.5700", "5. volume": "50214881"}, "2023-06-07": {"1. open": "178.4400", "2. high": "181.2100", "3. low": "177.3200", "4. close": "177.8200", "5. volume": "61944615"}, "2023-06-06": {"1. open": "179.9650", "2. high": "180.1200", "3. low": "177.4300", "4. close": "179.2100", "5. volume": "64848374"}, "2023-06-05": {"1. open": "182.6300", "2. high": "184.9510", "3. low": "178.0350", "4. close": "179.5800", "5. volume": "121946497"}, "2023-06-02": {"1. open": "181.0300", "2. high": "181.7800", "3. low": "179.2600", "4. close": "180.9500", "5. volume": "61996913"}, "2023-06-01": {"1. open": "177.7000", "2. high": "180.1200", "3. low": "176.9306", "4. close": "180.0900", "5. volume": "68901809"}, "2023-05-31": {"1. open": "177.3250", "2. high": "179.3500", "3. low": "176.7600", "4. close": "177.2500", "5. volume": "99313268"}, "2023-05-30": {"1. open": "176.9600", "2. high": "178.9900", "3. low": "176.5700", "4. close": "177.3000", "5. volume": "55964401"}, "2023-05-26": {"1. open": "173.3200", "2. high": "175.7700", "3. low": "173.1100", "4. close": "175.4300", "5. volume": "54834975"}, "2023-05-25": {"1. open": "172.4100", "2. high": "173.8950", "3. low": "171.6900", "4. close": "172.9900", "5. volume": "56058258"}, "2023-05-24": {"1. open": "171.0900", "2. high": "172.4183", "3. low": "170.5200", "4. close": "171.8400", "5. volume": "45143488"}, "2023-05-23": {"1. open": "173.1300", "2. high": "173.3794", "3. low": "171.2750", "4. close": "171.5600", "5. volume": "50747263"}, "2023-05-22": {"1. open": "173.9800", "2. high": "174.7100", "3. low": "173.4500", "4. close": "174.2000", "5. volume": "43570932"}, "2023-05-19": {"1. open": "176.3900", "2. high": "176.3900", "3. low": "174.9400", "4. close": "175.1600", "5. volume": "55809475"}, "2023-05-18": {"1. open": "173.0000", "2. high": "175.2400", "3. low": "172.5800", "4. close": "175.0500", "5. volume": "65496657"}, "2023-05-17": {"1. open": "171.7100", "2. high": "172.9250", "3. low": "170.4201", "4. close": "172.6900", "5. volume": "57951604"}, "2023-05-16": {"1. open": "171.9900", "2. high": "173.1383", "3. low": "171.7991", "4. close": "172.0700", "5. volume": "42110293"}, "2023-05-15": {"1. open": "173.1600", "2. high": "173.2100", "3. low": "171.4700", "4. close": "172.0700", "5. volume": "37266659"}, "2023-05-12": {"1. open": "173.6200", "2. high": "174.0600", "3. low": "171.0000", "4. close": "172.5700", "5. volume": "45533138"}, "2023-05-11": {"1. open": "173.8500", "2. high": "174.5900", "3. low": "172.1700", "4. close": "173.7500", "5. volume": "49514676"}, "2023-05-10": {"1. open": "173.0200", "2. high": "174.0300", "3. low": "171.9000", "4. close": "173.5550", "5. volume": "53724501"}, "2023-05-09": {"1. open": "173.0500", "2. high": "173.5400", "3. low": "171.6000", "4. close": "171.7700", "5. volume": "45326874"}, "2023-05-08": {"1. open": "172.4800", "2. high": "173.8500", "3. low": "172.1100", "4. close": "173.5000", "5. volume": "55962793"}, "2023-05-05": {"1. open": "170.9750", "2. high": "174.3000", "3. low": "170.7600", "4. close": "173.5700", "5. volume": "113453171"}, "2023-05-04": {"1. open": "164.8900", "2. high": "167.0400", "3. low": "164.3100", "4. close": "165.7900", "5. volume": "81235427"}, "2023-05-03": {"1. open": "169.5000", "2. high": "170.9200", "3. low": "167.1600", "4. close": "167.4500", "5. volume": "65136018"}, "2023-05-02": {"1. open": "170.0900", "2. high": "170.3500", "3. low": "167.5400", "4. close": "168.5400", "5. volume": "48425696"}, "2023-05-01": {"1. open": "169.2800", "2. high": "170.4500", "3. low": "168.6400", "4. close": "169.5900", "5. volume": "52472936"}, "2023-04-28": {"1. open": "168.4900", "2. high": "169.8500", "3. low": "167.8801", "4. close": "169.6800", "5. volume": "55275851"}, "2023-04-27": {"1. open": "165.1900", "2. high": "168.5600", "3. low": "165.1900", "4. close": "168.4100", "5. volume": "64902329"}, "2023-04-26": {"1. open": "163.0550", "2. high": "165.2800", "3. low": "162.8000", "4. close": "163.7600", "5. volume": "44105745"}, "2023-04-25": {"1. open": "165.1900", "2. high": "166.3050", "3. low": "163.7300", "4. close": "163.7700", "5. volume": "48714063"}, "2023-04-24": {"1. open": "165.0000", "2. high": "165.6000", "3. low": "163.8900", "4. close": "165.3300", "5. volume": "41949581"}, "2023-04-21": {"1. open": "165.0500", "2. high": "166.4521", "3. low": "164.4900", "4. close": "165.0200", "5. volume": "58337341"}, "2023-04-20": {"1. open": "166.0900", "2. high": "167.8700", "3. low": "165.5600", "4. close": "166.6500", "5. volume": "52456377"}, "2023-04-19": {"1. open": "165.8000", "2. high": "168.1600", "3. low": "165.5400", "4. close": "167.6300", "5. volume": "47720166"}, "2023-04-18": {"1. open": "166.1000", "2. high": "167.4100", "3. low": "165.6500", "4. close": "166.4700", "5. volume": "49923008"}, "2023-04-17": {"1. open": "165.0900", "2. high": "165.3900", "3. low": "164.0300", "4. close": "165.2300", "5. volume": "40713618"}, "2023-04-14": {"1. open": "164.5900", "2. high": "166.3200", "3. low": "163.8200", "4. close": "165.2100", "5. volume": "49386480"}, "2023-04-13": {"1. open": "161.6300", "2. high": "165.8000", "3. low": "161.4200", "4. close": "165.5600", "5. volume": "68445649"}, "2023-04-12": {"1. open": "161.2200", "2. high": "162.0600", "3. low": "159.7800", "4. close": "160.1000", "5. volume": "50133062"}, "2023-04-11": {"1. open": "162.3500", "2. high": "162.3600", "3. low": "160.5100", "4. close": "160.8000", "5. volume": "47644217"}, "2023-04-10": {"1. open": "161.4200", "2. high": "162.0300", "3. low": "160.0800", "4. close": "162.0300", "5. volume": "47716882"}, "2023-04-06": {"1. open": "162.4300", "2. high": "164.9584", "3. low": "162.0000", "4. close": "164.6600", "5. volume": "45390123"}, "2023-04-05": {"1. open": "164.7400", "2. high": "165.0500", "3. low": "161.8000", "4. close": "163.7600", "5. volume": "51511744"}, "2023-04-04": {"1. open": "166.5950", "2. high": "166.8400", "3. low": "165.1100", "4. close": "165.6300", "5. volume": "46278295"}}};
  
  const dailyData = dataObj["Time Series (Daily)"];
  
  const dates = Object.keys(dailyData);
  const opens = dates.map(date => parseFloat(dailyData[date]["1. open"]));
  const highs = dates.map(date => parseFloat(dailyData[date]["2. high"]));
  const lows = dates.map(date => parseFloat(dailyData[date]["3. low"]));
  const closes = dates.map(date => parseFloat(dailyData[date]["4. close"]));
  
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