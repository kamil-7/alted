import React from "react";
import Select from "react-select";
import "react-select/dist/react-select.css";

export default ({ input, meta: { touched, error } }) => (
  <label>
    Operator
    <Select
      options={globalData.operatorChoices}
      value={input.value}
      onChange={value => input.onChange(value.value)}
      onBlur={() => input.onBlur(input.value.value)}
      searchable={false}
    />
    {touched &&
      error && (
        <div className="form__error">
          <i className="material-icons form__error-icon">error</i>
          {error}
        </div>
      )}
  </label>
);
