import { saveSignal } from "./actions";
import { errorNotify, getOptions } from "./utils";
import * as axios from "axios";

export function saveSignalAsync(data) {
  return (dispatch, getState) => {
    // data = {
    //   name: data.name,
    //   conditionSet: data.conditions.map(condition => ({
    //     ...condition,
    //       id: condition.id,
    //       operator: condition.operator.value,
    //       target: condition.target.value,
    //       targetId: condition.target_identifier.id,
    //       value: condition.value
    //     }))
    // };
    //
    let data2 = data;
    axios
      .post("/api/signal-create/", data2, getOptions())
      .then(response => {
        dispatch(saveSignal(response));
        window.location = "/signals/?m=created";
      })
      .catch(error => {
        errorNotify("save an signal");
        console.log(error);
      });
  };
}
