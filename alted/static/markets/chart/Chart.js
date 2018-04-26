import React from "react";
import * as d3 from "d3";
import { withFauxDOM } from "react-faux-dom";

class MyReactComponent extends React.Component {
  componentDidMount() {
    const faux = this.props.connectFauxDOM("div", "chart");

    let margin = { top: 20, right: 20, bottom: 30, left: 50 },
      width = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;

    let svg = d3
      .select(faux)
      .append("svg")
      .attr("preserveAspectRatio", "xMinYMin meet")
      .attr("viewBox", "0 0 960 500")
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    this.props.animateFauxDOM(800);

    // parse the date / time
    let parseTime = d3.timeParse("%Y-%m-%d %H:%M:%S");

    // set the ranges
    let x = d3.scaleTime().range([0, width]);
    let y = d3.scaleLinear().range([height, 0]);

    // define the line
    let valueline = d3
      .line()
      .x(function(d) {
        return x(d[0]);
      })
      .y(function(d) {
        return y(d[1]);
      });

    // append the svg obgect to the body of the page
    // appends a 'group' element to 'svg'
    // moves the 'group' element to the top left margin

    // Get the data

    let data = globalData.chart;

    // format the data
    data.forEach(function(d) {
      d[0] = parseTime(d[0]);
      d[1] = +d[1];
    });

    // Scale the range of the data
    x.domain(
      d3.extent(data, function(d) {
        return d[0];
      })
    );
    y.domain([
      d3.min(data, d => {
        return d[1];
      }),
      d3.max(data, function(d) {
        return d[1];
      })
    ]);

    // Add the valueline path.
    svg
      .append("path")
      .data([data])
      .attr("class", "line")
      .attr("d", valueline);

    // Add the X Axis
    svg
      .append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    // Add the Y Axis
    svg.append("g").call(d3.axisLeft(y));
  }

  render() {
    return (
      <div>
        <div>{this.props.chart}</div>
      </div>
    );
  }
}

MyReactComponent.defaultProps = {
  chart: "loading"
};

export default withFauxDOM(MyReactComponent);
