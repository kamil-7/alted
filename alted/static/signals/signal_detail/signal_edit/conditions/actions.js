export const ADD_CONDITION = "ADD_CONDITION";
export const SAVE_CONDITION = "SAVE_CONDITION";
export const LOAD_CONDITIONS = "LOAD_CONDITIONS";
export const DELETE_CONDITION = "DELETE_CONDITION";

export function addCondition(signalId) {
  return {
    type: ADD_CONDITION,
    signalId: signalId
  };
}

export function saveCondition(signalId, conditionId) {
  return {
    type: SAVE_CONDITION,
    signalId: signalId,
    conditionId: conditionId
  };
}

export function deleteCondition(conditionId) {
  return {
    type: DELETE_CONDITION,
    conditionId: conditionId
  };
}
