import {
  ADD_CONDITION,
  SAVE_CONDITION,
  LOAD_CONDITIONS,
  DELETE_CONDITION
} from "./actions";
import omit from "lodash/omit";

const INITIAL_STATE = {};

// todo: froze store by https://github.com/rtfeldman/seamless-immutable

let conditionsReducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case LOAD_CONDITIONS:
      return { ...state, ...action.data };

    case ADD_CONDITION:
      return {
        ...state,
        ["-" + action.signalId.toString()]: {
          id: -action.signalId
        }
      };

    case SAVE_CONDITION:
      return {
        ...state
      };

    case DELETE_CONDITION:
      return omit(state, action.conditionId);

    default:
      return state;
  }
};

export default conditionsReducer;
