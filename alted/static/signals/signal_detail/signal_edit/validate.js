const validate = values => {
  const errors = {};
  if (!values.name) {
    errors.name = "Required";
  }
  if (!values.conditions || !values.conditions.length) {
    errors.conditions = { _error: "At least one condition must be entered" };
  } else {
    const conditionsArrayErrors = [];
    values.conditions.forEach((condition, conditionIndex ) => {
      const conditionErrors = {};
      ['target', 'target_identifier', 'operator', 'value'].forEach((field) => {
      if (!condition || !condition[field]) {
        conditionErrors[field] = "Required";
        conditionsArrayErrors[conditionIndex] = conditionErrors;
      }
      });
    });
    if (conditionsArrayErrors.length) {
      errors.conditions = conditionsArrayErrors;
    }
  }
  console.log(errors);
  return errors;
};

export default validate;
