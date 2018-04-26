import { saveSignal } from "./actions";
import { errorNotify, getOptions } from "./utils";
import * as axios from "axios";

export function updateSignalAsync(data) {
  return (dispatch, getState) => {
    data = {
      ...data,
      id: globalData.signal.id
    };
    axios
      .put(`/api/signal-update/${data.id}/`, data, getOptions())
      .then(response => {
        dispatch(saveSignal(response));
      })
      .catch(error => {
        errorNotify("save an signal");
        console.log(error);
      });
  };
}
