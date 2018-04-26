import SignalEdit from "./SignalEdit";
import { connect } from "react-redux";
import { updateSignalAsync } from "./asyncActions";

const mapStateToProps = state => {
  return {
    state: state,
    initialValues: globalData.signal
  };
};

const mapDispatchToProps = dispatch => {
  return {
    updateSignal: data => dispatch(updateSignalAsync(data))
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SignalEdit);
