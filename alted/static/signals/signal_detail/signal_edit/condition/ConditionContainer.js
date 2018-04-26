import Condition from "./Condition";
import { connect } from "react-redux";
import { getSafe } from "../utils";

const mapStateToProps = (state, props) => {
  return {
    targetType: getSafe(() => state.form.signal.values.conditionSet[props.index].targetType),
  };
};

export default connect(mapStateToProps)(Condition);
