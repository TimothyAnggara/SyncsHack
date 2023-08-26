import React from 'react';
import { Line } from 'react-chartjs-2';

const LineChartComponent = () => {
  const data = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [
        {
            label: 'Monthly Sales',
            data: [10, 20, 15, 30, 25, 35, 40],
            fill: false,
            borderColor: 'blue',
            tension: 0.1
        }
    ]
};

return (<div>
        <Line data={data} />;
      </div>
)

}

export default LineChartComponent;
