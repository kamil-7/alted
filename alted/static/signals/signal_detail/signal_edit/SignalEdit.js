import React from "react";
import { Field, FieldArray, reduxForm } from "redux-form";
import validate from "./validate";
import conditions from "./conditions/Conditions";
import { renderField } from "./utils";

const SignalEdit = props => {
  const { handleSubmit, updateSignal, submitting } = props;
  return (
    <div className="signals">
      <h2 className="signals__section">Signal Edit</h2>
      <form onSubmit={handleSubmit(data => updateSignal(data))}>
        <Field
          className="signals__section"
          name="name"
          type="text"
          component={renderField}
          label="Name"
        />
        <FieldArray name="conditionSet" component={conditions} />
        <div className="signals__section signal-create__section--last">
          <button
            type="submit"
            className="signal-create__save-button mdl-button mdl-js-button mdl-button--raised mdl-button--primary mdl-js-ripple-effect"
            disabled={submitting}
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  );
};

export default reduxForm({
  form: "signal", // a unique identifier for this form
  fields: ["signal.conditionSet[].id"],
  validate
})(SignalEdit);
