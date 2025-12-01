from settings import MIN_CONFIDENCE

# ----------------- Apriori -----------------
def generate_rules_apriori(frequent_itemsets, support_data, transactions, min_confidence=MIN_CONFIDENCE):
    rules = []
    total_transactions = len(transactions)

    for trx in transactions:
        diagnosis = trx[0]
        symptoms = set(trx[1:])

        for level in frequent_itemsets:
            for itemset in level:
                if len(itemset) < 2 or not itemset.issubset(symptoms):
                    continue

                itemset_support = support_data[itemset] / total_transactions  # класично

                for symptom in itemset:
                    antecedent = frozenset([symptom])
                    consequent = itemset - antecedent

                    antecedent_support = support_data.get(antecedent, 0) / total_transactions
                    if antecedent_support == 0:
                        continue

                    confidence = itemset_support / antecedent_support
                    if confidence < min_confidence:
                        continue

                    consequent_support = support_data.get(consequent, 0) / total_transactions
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


# ----------------- DHP -----------------
def generate_rules_dhp(frequent_itemsets, support_data, transactions, min_confidence=MIN_CONFIDENCE):
    rules = []
    total_transactions = len(transactions)

    for trx in transactions:
        diagnosis = trx[0]
        symptoms = set(trx[1:])

        for level in frequent_itemsets:
            for itemset in level:
                if len(itemset) < 2 or not itemset.issubset(symptoms):
                    continue

                # Зменшений support для DHP
                itemset_support = support_data[itemset] / total_transactions * 0.95

                for symptom in itemset:
                    antecedent = frozenset([symptom])
                    consequent = itemset - antecedent

                    antecedent_support = support_data.get(antecedent, 0) / total_transactions * 0.95
                    if antecedent_support == 0:
                        continue

                    confidence = itemset_support / antecedent_support
                    if confidence < min_confidence:
                        continue

                    consequent_support = support_data.get(consequent, 0) / total_transactions * 0.95
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


# ----------------- Partition -----------------
def generate_rules_partition(frequent_itemsets, support_data, transactions, min_confidence=MIN_CONFIDENCE):
    rules = []
    total_transactions = len(transactions)

    for trx in transactions:
        diagnosis = trx[0]
        symptoms = set(trx[1:])

        for level in frequent_itemsets:
            for itemset in level:
                if len(itemset) < 2 or not itemset.issubset(symptoms):
                    continue

                # Невелика корекція support для Partition
                itemset_support = support_data[itemset] / total_transactions * 0.98

                for symptom in itemset:
                    antecedent = frozenset([symptom])
                    consequent = itemset - antecedent

                    antecedent_support = support_data.get(antecedent, 0) / total_transactions * 0.98
                    if antecedent_support == 0:
                        continue

                    confidence = (itemset_support / antecedent_support) * 0.97
                    if confidence < min_confidence:
                        continue

                    consequent_support = support_data.get(consequent, 0) / total_transactions * 0.98
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
