import React from "react";
import ReactDOM from "react-dom";
import { applyMiddleware, compose, createStore } from "redux";
import { Provider } from "react-redux";
import reducers from "./signal_edit/reducers";
import SignalEditContainer from "./signal_edit/SignalEditContainer";
import thunk from "redux-thunk";

const finalCreateStore = compose(applyMiddleware(thunk))(createStore);

let store = finalCreateStore(
  reducers,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);

if (module.hot) {
  // Enable Webpack hot module replacement for reducers
  module.hot.accept("./signal_edit/reducers", () => {
    const nextRootReducer = require("./signal_edit/reducers");
    store.replaceReducer(nextRootReducer);
  });
}

const place = document.getElementsByClassName("signal-detail-component")[0];

ReactDOM.render(
  <Provider store={store}>
    <SignalEditContainer />
  </Provider>,
  place
);
