from settings import MIN_CONFIDENCE
from itertools import combinations

def generate_rules_ais(frequent_itemsets, support_data, transactions, min_confidence=MIN_CONFIDENCE):
    rules = []
    total_transactions = len(transactions)

    for trx in transactions:
        diagnosis = trx[0]
        symptoms = set(trx[1:])

        for itemset in frequent_itemsets:
            if not isinstance(itemset, (set, frozenset)):
                continue
            if len(itemset) < 2 or not itemset.issubset(symptoms):
                continue

            # імітація ваги для AIS
            itemset_support = support_data[itemset] / total_transactions * 1.1

            for symptom in itemset:
                antecedent = frozenset([symptom])
                consequent = itemset - antecedent

                antecedent_support = support_data.get(antecedent, 0) / total_transactions * 1.1
                if antecedent_support == 0:
                    continue

                confidence = itemset_support / antecedent_support
                if confidence < min_confidence:
                    continue

                consequent_support = support_data.get(consequent, 0) / total_transactions * 1.1
                lift = confidence / consequent_support if consequent_support > 0 else 0

                rules.append({
                    "diagnosis": diagnosis,
                    "antecedent": list(antecedent),
                    "consequent": list(consequent),
                    "support": itemset_support,
                    "confidence": confidence,
                    "lift": lift
                })
    return rules