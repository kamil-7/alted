import { connect } from "react-redux";
import Coin from "./Coin";
import { fetchCoin } from "./actions";

const mapStateToProps = state => {
  return state.coin;
};

const mapDispatchToProps = dispatch => {
  return {
    fetchCoin: () => {
      dispatch(fetchCoin());
    }
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Coin);
