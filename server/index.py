from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import csv
from pydantic import BaseModel
from typing import List
from settings import CSV_FILE, MIN_SUPPORT, MIN_CONFIDENCE
from load_symptoms import load_symptoms
from load_transactions import load_transactions
from combine_rules import combine_all_rules

app = FastAPI(title="Symptoms API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # дозволити всім
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SymptomsRequest(BaseModel):
    symptoms: List[str]


SYMPTOMS_LIST = load_symptoms()


@app.get("/symptoms")
def get_symptoms():
    """
    Returns a JSON list of all unique symptoms.
    """
    return {"symptoms": SYMPTOMS_LIST}

@app.post("/process-symptoms")
def process_symptoms(data: SymptomsRequest):
    selected = [s.strip() for s in data.symptoms]
    
    ALL_TRANSACTIONS = load_transactions()

    # 1) Фільтруємо рядки з CSV
    matching = []
    for row in ALL_TRANSACTIONS:
        row_symptoms = [s.strip() for s in row[1:] if s.strip()]
        if sum(1 for s in selected if s in row_symptoms) >= 2:
            matching.append([row[0], *row_symptoms])

    results = combine_all_rules(matching, selected)
    return results
    
    



