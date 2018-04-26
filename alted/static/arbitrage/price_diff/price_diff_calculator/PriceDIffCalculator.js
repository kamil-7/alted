import React, { Component } from "react";


class PriceDiffCalculator extends Component {
  constructor() {
    super();
    this.state = {}
  }

  update = (bottom, top) => {
    this.setState({
      top: parseFloat(top),
      bottom: parseFloat(bottom),
    })
  };

  render() {
    let {top, bottom } = this.state;
    let diff = (top / bottom - 1) * 100;
    let gap = (diff - 1) / 2;
    let maxBuy = bottom + bottom * (gap / 100);
    let minSell = top - top * (gap / 100);

    return (
      <div>
        {/*<input type="text" onInput={(e) => this.setState({top: parseFloat(e.target.value)})} value={this.state.top} />*/}
        {/*<input type="text" onInput={(e) => this.setState({bottom: parseFloat(e.target.value)})} value={this.state.bottom} />*/}
        <div>Max buy:  {maxBuy}</div>
        <div>Min sell: {minSell}</div>
        <div>Diff: {diff} %</div>
      </div>
    )
  }
}

export default PriceDiffCalculator;
