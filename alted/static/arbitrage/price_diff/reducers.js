import {FETCHING_COIN_SUCCESS} from "./actions";

const initialState = {
  coin: globalData.coin,
  markets: globalData.markets
};

const coinReducer = (state = initialState, action) => {
  switch (action.type) {
    case FETCHING_COIN_SUCCESS:
      return {
        ...state,
        coin: action.data,
      };
    default:
      return state;
  }
};

export default coinReducer;
