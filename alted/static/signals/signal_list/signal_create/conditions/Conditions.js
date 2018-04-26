import React, { Component } from "react";
import Condition from "../condition/ConditionContainer";

const conditions = ({ fields }) => (
  <div>
    <div>
      {fields.map((condition, index) => (
        <Condition
          condition={condition}
          fields={fields}
          index={index}
          key={index}
        />
      ))}
    </div>
    <div className="signals__section signals__section">
      <button
        className="mdl-button mdl-js-button mdl-button--raised mdl-button--primary mdl-js-ripple-effect"
        type="button"
        onClick={() => fields.push({})}
      >
        Add another condition
      </button>
    </div>
  </div>
);

export default conditions;
