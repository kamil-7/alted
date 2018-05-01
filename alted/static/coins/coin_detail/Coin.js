import React, {Component} from "react";
import {Tab, TabList, TabPanel, Tabs} from "react-tabs";
import MarketsContainer from "../markets/MarketsContainer";
import numeral from "numeral";
import Chart from "../chart/Chart";

import "../chart/Chart.js";

class Coin extends Component {
  updateCoin = () => {
    this.props.fetchCoin();
    setTimeout(this.updateCoin, 60000);
  };

  componentDidMount = () => {
    this.updateCoin();
  };

  render() {
    return (
      <div>
        <div className="mdl-grid coin__header">
          <div className="mdl-cell mdl-cell--6-col coin__header-cell">
            <div>Price</div>
            <div className="coin__usd">{numeral(this.props.price_usd).format('$0,0.00')}</div>
            <div className="coin__btc">{this.props.price_btc} BTC</div>
          </div>
          <div className="mdl-cell mdl-cell--6-col coin__header-cell">
            <div>24h Volume</div>
            <div className="coin__usd">{numeral(this.props.volume_usd).format('$0,0.00')}</div>
            <div className="coin__btc">{this.props.volume_btc} BTC</div>
          </div>
        </div>
        <Tabs className="mdl-tabs mdl-tabs mdl-js-tabs mdl-js-ripple-effect">
          <TabList className="mdl-tabs__tab-bar">
            <Tab selectedClassName="is-active" className="mdl-tabs__tab">
              Chart
            </Tab>
            <Tab selectedClassName="is-active" className="mdl-tabs__tab">
              Markets
            </Tab>
          </TabList>
          <TabPanel>
            <Chart />
          </TabPanel>
          <TabPanel>
            <MarketsContainer />
          </TabPanel>
        </Tabs>
      </div>
    );
  }
}

export default Coin;
