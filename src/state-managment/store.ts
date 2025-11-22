import { legacy_createStore as createStore } from "redux";
import { symptomsReducer } from "./reducer";

export const store = createStore(symptomsReducer);

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
