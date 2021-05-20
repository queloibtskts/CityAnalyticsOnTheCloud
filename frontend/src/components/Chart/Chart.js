import React from "react";
import Chart from "react-google-charts";
const ColumnChart = ({data}) => (
  <div>
    <div style={{ display: 'flex', maxWidth: 900 }}>
      <Chart
        width={900}
        height={600}
        chartType="ColumnChart"
        loader={<div>Loading Chart</div>}
        data={data}
        options={{
          title: 'Top 3 popular vulgar words in each state',
          chartArea: { width: '60%' },
          hAxis: {
            title:  'State',
            minValue: 0,
          },
          vAxis: {
            title: 'Frequence',
            minValue: 0,
          },
          bar: { groupWidth: "70%" }
        }}
        legendToggle
      />
    </div>
  </div>
)

export default ColumnChart;