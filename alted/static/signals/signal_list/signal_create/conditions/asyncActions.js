import some from "lodash/some";
import * as axios from "axios";

import { errorNotify } from "../utils";
import { addCondition, saveCondition, deleteCondition } from "./actions";

export function addConditionAsync(signalId, conditionsIds) {
  return dispatch => {
    if (some(conditionsIds, key => key < 0)) {
      window.nos.addNotification({
        message:
          "Cannot add another condition, save or delete previously added condition",
        level: "error",
        position: "br"
      });
    } else {
      return dispatch(addCondition(signalId));
    }
  };
}

export function saveConditionAsync(values, signalId) {
  return dispatch => {
    delete values.target_data;
    let payload = {
      ...values,
      targetId: _.get(
        values.targetId,
        "id",
        values.targetId
      ),
      operator: _.get(values.operator, "value", values.operator),
      targetType: _.get(values.target, "value", values.targetType),
      signal_id: signalId
    };

    if (values.id < 0) {
      axios
        .post("/api/conditions/", payload)
        .then(response => {
          window.nos.addNotification({
            message: "Condition saved",
            level: "success",
            position: "br"
          });
          dispatch(saveCondition(signalId, response.id));
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      axios
        .put(`/api/conditions/${values.id}/`, payload)
        .then(response => {
          window.nos.addNotification({
            message: "Condition saved",
            level: "success",
            position: "br"
          });
          dispatch(saveCondition(signalId, response.id));
        })
        .catch(error => {
          console.log(error);
          errorNotify("save the condition");
        });
    }
  };
}
