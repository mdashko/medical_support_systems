from typing import List, Tuple
import pandas as pd
from settings import CSV_FILE

def load_transactions():
    df_from_csv = pd.read_csv(CSV_FILE, sep=',')
    
    transactions = []
    for _, row in df_from_csv.iterrows():
        items = [item for col, item in row.items() if pd.notna(item)]
        transactions.append(items)

    return transactions
