import { combineReducers } from "redux";
import conditionsReducer from "./conditions/reducers";
import { reducer as reduxFormReducer } from "redux-form";

const reducer = combineReducers({
  conditions: conditionsReducer,
  form: reduxFormReducer,
});

export default reducer;
