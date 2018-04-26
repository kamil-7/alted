import SignalCreate from "./SignalCreate";
import { connect } from "react-redux";
import { saveSignalAsync } from "./asyncActions";

const mapStateToProps = state => {
  return {
    state: state,
    initialValues: {
      conditionSet: [{}]
    }
  };
};

const mapDispatchToProps = dispatch => {
  return {
    saveSignal: data => dispatch(saveSignalAsync(data))
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SignalCreate);
