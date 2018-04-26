import React, {Component} from "react";
import {applyMiddleware, compose, createStore} from "redux";
import ReactDOM from "react-dom";
import {Provider} from "react-redux";
import promiseMiddleware from "redux-promise";
import thunk from 'redux-thunk'

import coinsReducer from "./reducers";
import PriceDiff from "./PriceDiff";

// const finalCreateStore = compose(
//   applyMiddleware(promiseMiddleware),
//   applyMiddleware(thunk),
// )(createStore);

// let store = finalCreateStore(coinsReducer, window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__());

if (module.hot) {
  // Enable Webpack hot module replacement for reducers
  module.hot.accept('./reducers', () => {
    const nextRootReducer = require('./reducers');
    store.replaceReducer(nextRootReducer);
  });
}

const place = document.getElementsByClassName('price-diff-component')[0];
ReactDOM.render(<PriceDiff />, place);

// export default store;
