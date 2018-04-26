import React, { Component } from "react";

class Markets extends Component {
  render() {
    return (
      <table className="markets mdl-data-table mdl-js-data-table mdl-shadow--2dp">
        <thead>
          <tr>
            <th className="mdl-data-table__cell--non-numeric">Market</th>
            <th>Price</th>
            <th>Volume 24h in BTC</th>
            <th>Volume 24h in USD</th>
          </tr>
        </thead>
        <tbody>
          {this.props.markets.map((market, i) => (
            <tr key={i}>
              <td className="mdl-data-table__cell--non-numeric">
                <a href="">{market.name}</a>
              </td>
              <td>{market.price}</td>
              <td>{market.volume_btc} BTC</td>
              <td>{market.volume_usd}</td>
            </tr>
          ))}
        </tbody>
      </table>
    );
  }
}

export default Markets;
