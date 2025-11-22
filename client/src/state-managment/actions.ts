export const ADD_SYMPTOM = "ADD_SYMPTOM";
export const REMOVE_SYMPTOM = "REMOVE_SYMPTOM";

export interface AddSymptomAction {
    type: typeof ADD_SYMPTOM;
    payload: string;
}

export interface RemoveSymptomAction {
    type: typeof REMOVE_SYMPTOM;
    payload: string;
}

export function addSymptom(symptom: string): AddSymptomAction {
    return {
        type: ADD_SYMPTOM,
        payload: symptom,
    };
}

export function removeSymptom(symptom: string): RemoveSymptomAction {
    return {
        type: REMOVE_SYMPTOM,
        payload: symptom,
    };
}

export type SymptomsListActions = AddSymptomAction | RemoveSymptomAction;

