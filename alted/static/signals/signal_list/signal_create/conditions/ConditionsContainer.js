import Conditions from "./Conditions";
import { connect } from "react-redux";
import {addSignalCondition} from "../actions";
import {addConditionAsync} from "./asyncActions";

const mapStateToProps = state => {
  return {
    conditions: state.conditions
  };
};

const mapDispatchToProps = dispatch => {
  return {
    addContidion: (signalId, conditionsIds) => dispatch(addConditionAsync(signalId, conditionsIds)),
    addSignalCondition: (signalId) => dispatch(addSignalCondition(signalId)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Conditions);
