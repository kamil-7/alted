import * as axios from "axios";

const MARKET_DETAIL_URL = "http:///127.0.0.1:8000/api/market-detail/";


export const FETCHING_MARKET_SUCCESS = 'FETCHING_MARKET_SUCCESS';

export function fetchMarketSuccess(data) {
  return {
    type: FETCHING_MARKET_SUCCESS,
    data: data
  }
}

export function fetchMarket() {
  return (dispatch, getState) => {
    let id = getState().id;
    axios
      .get(`${MARKET_DETAIL_URL}${id}/`)
      .then(response => {
        dispatch(fetchMarketSuccess(response.data))
      })
      .catch(error => {
        console.log(error)
      })
  }
}
