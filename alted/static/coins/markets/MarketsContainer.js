import { connect } from "react-redux";
import Markets from "./Markets";

const mapStateToProps = state => {
  return {
    markets: state.markets,
  }
};

export default connect(mapStateToProps)(Markets);
