import * as axios from "axios";

const COIN_DETAIL_URL = "http:///127.0.0.1:8000/api/coin-detail/";


export const FETCHING_COIN_SUCCESS = 'FETCHING_COIN_SUCCESS';

export function fetchCoinSuccess(data) {
  return {
    type: FETCHING_COIN_SUCCESS,
    data: data
  }
}

export function fetchCoin() {
  return (dispatch, getState) => {
    let slug = getState().coin.slug;
    axios
      .get(`${COIN_DETAIL_URL}${slug}/`)
      .then(response => {
        dispatch(fetchCoinSuccess(response.data))
      })
      .catch(error => {
        console.log(error)
      })
  }
}
