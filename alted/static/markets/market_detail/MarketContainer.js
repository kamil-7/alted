import { connect } from "react-redux";
import Market from "./Market";
import { fetchMarket } from "./actions";

const mapStateToProps = state => {
  return state.market;
};

const mapDispatchToProps = dispatch => {
  return {
    fetchMarket: () => {
      dispatch(fetchMarket());
    }
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Market);
