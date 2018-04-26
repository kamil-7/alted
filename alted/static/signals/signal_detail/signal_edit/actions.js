export const FETCH_SIGNALS = "FETCH_SIGNALS";
export const LOAD_SIGNALS = "LOAD_SIGNALS";
export const LOAD_SIGNAL_FORM = "LOAD_SIGNAL_FORM";
export const ADD_SIGNAL_CONDITION = "ADD_SIGNAL_CONDITION";
export const DELETE_SIGNAL_CONDITION = "DELETE_SIGNAL_CONDITION";
export const SAVE_SIGNAL = "SAVE_SIGNAL";

export function addSignalCondition(signalId) {
  return {
    type: ADD_SIGNAL_CONDITION,
    signalId: signalId
  };
}

export function saveSignal(signalId) {
  return {
    type: SAVE_SIGNAL,
    signalId: signalId,
  }
}

export function deleteSignalCondition(signalId, conditionId) {
  return {
    type: DELETE_SIGNAL_CONDITION,
    signalId: signalId,
    conditionId: conditionId
  };
}
