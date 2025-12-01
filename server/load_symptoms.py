import csv
from settings import CSV_FILE

def load_symptoms():
    symptoms_set = set()

    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            for key in ["symptom1", "symptom2", "symptom3", "symptom4", "symptom5"]:
                value = row.get(key)
                if value and value.strip():
                    symptoms_set.add(value.strip())

    return sorted(list(symptoms_set))


