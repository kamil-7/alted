import React, { Component } from "react";
import { Async } from "react-select";
import * as axios from "axios";

class ConditionValueIdentifierField extends Component {
  loadObjects = input => {
    let target = this.props.targetType;
    if (isNaN(this.props.targetType)) {
      target = target.value;
    }
    return axios
      .get("/api/target-list?target=" + target + "&q=" + input)
      .then(function(response) {
        return { options: response.data };
      })
      .catch(function(error) {
        console.log(error);
      });
  };

  render = () => {
    let { meta: { touched, error } } = this.props;
    return (
      <div className="section">
        <label>
          Element
          <Async
            {...this.props}
            value={this.props.input.value}
            onChange={value => this.props.input.onChange(value.value)}
            valueKey="id"
            labelKey="name"
            loadOptions={this.loadObjects}
            backspaceRemoves={true}
          />
          {touched &&
            error && (
              <div className="form__error">
                <i className="material-icons form__error-icon">error</i>
                {error}
              </div>
            )}
        </label>
      </div>
    );
  };
}

export default ConditionValueIdentifierField;
