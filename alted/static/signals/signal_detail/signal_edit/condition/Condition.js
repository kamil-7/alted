import React, { Component } from "react";
import { reduxForm, Field } from "redux-form";
import ConditionTargetTypeField from "../fields/conditionTargetTypeField";
import ConditionOperatorField from "../fields/conditionOperatorField";
import ConditionValueIdentifierField from "../fields/conditionValueIdentifierField";
import {renderField} from "../utils";

class Condition extends Component {
  // todo: reduxform condition choices
  render = () => {
    let { condition, index, fields } = this.props;
    return (
      <div className="signals__section">
        <button
          type="button"
          className="signals__remove-condition clearfix mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect"
          title="Remove Condition"
          onClick={() => fields.remove(index)}
        >
          <i className="material-icons">delete</i>
        </button>
        <h3 className="signal-create__header">Condition {index + 1}</h3>
        <div className="signal__field">
          <Field
            name={`${condition}.targetType`}
            component={ConditionTargetTypeField}
          />
        </div>
        {this.props.targetType && (
          <div className="signal__field">
            <Field
              name={`${condition}.targetId`}
              component={ConditionValueIdentifierField}
              targetType={this.props.targetType}
            />
          </div>
        )}
        <div className="signal__field">
          <Field
            name={`${condition}.operator`}
            component={ConditionOperatorField}
          />
        </div>
        <div className="signal__field">
          <label>
            Value
            <Field
              name={`${condition}.value`}
              component={renderField}
              type="number"
            />
          </label>
        </div>
      </div>
    );
  };
}

export default Condition;
