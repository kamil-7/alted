import React, { Component } from "react";
import { Tab, TabList, TabPanel, Tabs } from "react-tabs";
import numeral from "numeral";
import Chart from "../chart/Chart";

class Market extends Component {
  updateMarket = () => {
    this.props.fetchMarket();
    setTimeout(this.updateMarket, 10000);
  };

  componentDidMount = () => {
    this.updateMarket();
  };

  render() {
    return (
      <div>
        <div className="mdl-grid">
          <div className="mdl-cell mdl-cell--4-col market__price">
            <h2>{numeral(this.props.price).format('0,0.00000000')}</h2>
            <span>Last Price</span>
          </div>
          <div className="mdl-cell mdl-cell--4-col market__price">
            <h2>{numeral(this.props.volume_usd).format('$0,0.00')}</h2>
            <span>Volume in USD</span>
          </div>
          <div className="mdl-cell mdl-cell--4-col market__price">
            <h2>{numeral(this.props.volume_btc).format('0,0.000')}</h2>
            <span>Volume in BTC</span>
          </div>
        </div>
        <Tabs className="mdl-tabs">
          <TabList className="mdl-tabs__tab-bar">
            <Tab selectedClassName="is-active" className="mdl-tabs__tab">
              <Chart />
            </Tab>
          </TabList>
          <TabPanel className="mdl-tabs__panel">this is chart</TabPanel>
        </Tabs>
      </div>
    );
  }
}

export default Market;
