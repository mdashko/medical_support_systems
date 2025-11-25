from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import csv
from pydantic import BaseModel
from typing import List

CSV_FILE = "symptoms_diseases.csv"

app = FastAPI(title="Symptoms API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Модель для прийому симптомів
class SymptomsRequest(BaseModel):
    symptoms: List[str]

def load_unique_symptoms():
    symptoms_set = set()

    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            for key in ["симптом1", "симптом2", "симптом3", "симптом4", "симптом5"]:
                value = row.get(key)
                if value and value.strip():
                    symptoms_set.add(value.strip())

    return sorted(list(symptoms_set))


SYMPTOMS_LIST = load_unique_symptoms()


@app.get("/symptoms")
def get_symptoms():
    """
    Returns a JSON list of all unique symptoms.
    """
    return {"symptoms": SYMPTOMS_LIST}

@app.post("/process-symptoms")
def process_symptoms(data: SymptomsRequest):
    selected = data.symptoms
	

    # --- тут ти можеш передати симптоми у будь-який метод ---
    # Приклади:
    # result = find_diseases_by_symptoms(selected)
    # result = run_association_model(selected)
    # result = predict_disease(selected)
    # ---------------------------------------------------------

    return {
        "received_symptoms": selected,
        "message": "Symptoms successfully processed"
    }