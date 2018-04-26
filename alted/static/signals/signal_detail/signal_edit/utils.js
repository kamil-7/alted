import cookie from "react-cookie";
import React from "react";

const getSafe = function(fn) {
  try {
    return fn();
  } catch (e) {
    return undefined;
  }
};

const getOptions = function() {
  return {
    headers: {
      "x-csrftoken": cookie.load("csrftoken"),
      sessionid: cookie.load("sessionid")
    }
  };
};

const errorNotify = function(action) {};

const renderField = ({
  input,
  label,
  type,
  className,
  meta: { touched, error }
}) => (
  <div className={className}>
    <label>{label}</label>
    <div>
      <input className="input" {...input} type={type} placeholder={label} />
      {touched &&
        error && (
          <div className="form__error">
            <i className="material-icons form__error-icon">error</i>
            {error}
          </div>
        )}
    </div>
  </div>
);

export { getSafe, getOptions, errorNotify, renderField };
