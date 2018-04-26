import React, {Component} from "react";
import * as d3 from "d3";
import "d3-selection-multi";
import {withFauxDOM} from "react-faux-dom";

import PriceDiffCalculator from './price_diff_calculator/PriceDIffCalculator';

class MyReactComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {};
    this.parseTime = d3.timeParse("%Y-%m-%d %H:%M:%S");
    this.firstPointValue = null;

    this.priceChart = {
      data: []
    }
  }


  handlePointClick = (value) => {
    if (this.firstPointValue) {
      this.refs.calculator.update(this.firstPointValue, value)
      this.firstPointValue = null;
    } else {
      this.firstPointValue = value;
    }
  };

  update = () => {
    let {svg, data} = this.priceChart;

    var minDate = globalData.chart[0][0];
    var maxDate = globalData.chart[globalData.chart.length - 1][0];
    let x = d3.scaleTime()
      .domain([minDate, maxDate])
      .range([0, this.priceChart.width]);

    svg.selectAll("g.x-axis").call(d3.axisBottom(x));

    svg.selectAll(".myline")
      .attr("d", this.priceChart.line(data));

    this.props.animateFauxDOM(800);
  };


  renderPriceChart = () => {
    const faux = this.props.connectFauxDOM("div", "priceChart");


    this.props.animateFauxDOM(800);

    let margin = {top: 20, right: 20, bottom: 30, left: 50},
      width = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;

    this.priceChart.width = width;

    this.priceChart.svg = d3.select(faux)
      .append("svg")
      .attr("preserveAspectRatio", "xMinYMin meet")
      .attr("viewBox", "0 0 960 500")
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    let {svg} = this.priceChart;

    var x = d3.scaleTime()
      .domain([globalData.chart[0][0], globalData.chart[globalData.chart.length - 1][0]])
      .range([0, width]);

    svg.append("g")
      .attr("class", "x-axis axis")
      .attr("transform", "translate(0 , " + height + ")")
      .call(d3.axisBottom(x));

    var y = d3.scaleLinear()
      .domain([30000, 40000])
      .range([height, 0]);

    svg.append("g")
      .attr("class", "axis")
      .call(d3.axisLeft(y));

    this.priceChart.line = d3.line()
      .x(function (d) {
        return x(d[0]);
      })
      .y(function (d) {
        return y(d[1]);
      });

    svg.append("path")
      .attr("class", "myline")
  };

  componentDidMount = () => {
    const faux = this.props.connectFauxDOM("div", "chart");

    let margin = {top: 20, right: 20, bottom: 30, left: 50},
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


    // set the ranges
    let x = d3.scaleTime().range([0, width]);
    let y = d3.scaleLinear().range([height, 0]);

    // define the line
    let buyValueline = d3
      .line()
      .x((d) => {
        return x(d[0]);
      })
      .y((d) => {
        return y(d[1]);
      });

    let sellValueline = d3
      .line()
      .x((d) => {
        return x(d[0]);
      })
      .y((d) => {
        return y(d[2]);
      });


    // append the svg obgect to the body of the page
    // appends a 'group' element to 'svg'
    // moves the 'group' element to the top left margin

    // Get the data

    let data = globalData.chart;

    // format the data
    data.forEach((d) => {
      d[0] = this.parseTime(d[0]);
      // d[1] = +d[1];
    });

    // Scale the range of the data
    x.domain(
      d3.extent(data, (d) => {
        return d[0];
      })
    );
    y.domain([
      d3.min(data, d => {
        return Math.min(d[1], d[2]);
      }),
      d3.max(data, (d) => {
        return Math.max(d[1], d[2]);
      })
    ]);

    // Add the valueline path.
    svg
      .append("path")
      .data([data])
      .attr("class", "price-diff__sell-line")
      .attr("d", buyValueline);

    svg
      .append("path")
      .data([data])
      .attr("class", "price-diff__buy-line")
      .attr("d", sellValueline);


    let div = d3.select("body").append("div")
      .attr("class", "tooltip")
      .style("opacity", 0);

    svg.selectAll("dot")
      .data(data)
      .enter().append("circle")
      .attr("r", 5)
      .attr("class", "price-diff__point")
      .attr("cx", (d) => {
        return x(d[0]);
      })
      .attr("cy", (d) => {
        return y(d[1]);
      })
      .on("mouseover", (d) => {
        div.transition()
          .duration(200)
          .style("opacity", 1);
        div.html(d[3])
          .style("left", (d3.event.pageX) + "px")
          .style("top", (d3.event.pageY - 28) + "px");
      })
      .on("mouseout", (d) => {
        div.transition()
          .duration(500)
          .style("opacity", 0);
      })
      .on("click", (d) => {
        this.priceChart.data.push([d[0], d[3]]);
        this.update();
        this.handlePointClick(d[3])
      });

    // Add the X Axis
    svg
      .append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    // Add the Y Axis
    svg.append("g").call(d3.axisLeft(y));
    this.renderPriceChart();
  };

  render = () => {
    return (
      <div>
        <div>{this.props.chart}</div>
        <div>{this.props.priceChart}</div>
        <PriceDiffCalculator ref="calculator" />
      </div>
    );
  }
}

MyReactComponent.defaultProps = {
  chart: "loading",
  priceChart: "loading"
};

export default withFauxDOM(MyReactComponent);
