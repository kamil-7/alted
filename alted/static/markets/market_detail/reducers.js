import {FETCHING_MARKET_SUCCESS} from "./actions";

const initialState = {
  market: globalData.market,
};

const marketReducer = (state = initialState, action) => {
  switch (action.type) {
    case FETCHING_MARKET_SUCCESS:
      return {
        ...state,
        market: action.data
      };
    default:
      return state;
  }
};

export default marketReducer;
