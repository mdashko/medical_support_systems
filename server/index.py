from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI(title="Illness List API")

# Allow all origins (for frontend requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to your CSV file
CSV_FILE = "diseases.csv"

# Load disease names once on startup
def load_diseases():
    diseases = set()
    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            disease_name = row.get("disease") or row.get("хвороба")
            if disease_name:
                diseases.add(disease_name.strip())
    return sorted(list(diseases))

DISEASE_LIST = load_diseases()

@app.get("/illnesses")
def get_illnesses():
    """
    Returns a JSON list of all unique illness names from the CSV.
    """
    return {"illnesses": DISEASE_LIST}
