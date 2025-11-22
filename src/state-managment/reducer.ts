import { ADD_SYMPTOM, REMOVE_SYMPTOM, SymptomsListActions } from "./actions";

interface SymptomsState {
    symptoms: string[];
}

const initialState: SymptomsState = {
    symptoms: []
};

export function symptomsReducer(
    state = initialState,
    action: SymptomsListActions
): SymptomsState {
    switch (action.type) {
        case ADD_SYMPTOM:
            return {
                ...state,
                symptoms: [...state.symptoms, action.payload]
            };
        case REMOVE_SYMPTOM:
            return {
                ...state,
                symptoms: state.symptoms.filter(s => s !== action.payload)
            };

        default:
            return state;
    }
}
