from copy import deepcopy

def get_frequent_itemsets_ais(transactions, min_support=2):
    total_transactions = len(transactions)
    frequent_itemsets = []
    support_data = {}

    # Частота окремих елементів
    item_count = {}
    for transaction in transactions:
        for item in transaction:
            key = frozenset([item])
            item_count[key] = item_count.get(key, 0) + 1

    # Часті 1-елементні множини
    L = set()
    for itemset, count in item_count.items():
        if count >= min_support:
            L.add(itemset)
            support_data[itemset] = count

    # Ініціалізація кроку з частими одиничками
    current_candidates = deepcopy(L)

    while current_candidates:
        new_candidates = set()

        for transaction in transactions:
            transaction_items = set(transaction)

            for candidate in current_candidates:
                if candidate.issubset(transaction_items):
                    # Пробуємо додати інші елементи до кандидата
                    for item in transaction_items:
                        new_candidate = candidate.union([item])
                        if len(new_candidate) == len(candidate) + 1:
                            new_candidates.add(new_candidate)

        candidate_count = {}
        for candidate in new_candidates:
            for transaction in transactions:
                if candidate.issubset(transaction):
                    candidate_count[candidate] = candidate_count.get(candidate, 0) + 1

        current_candidates = set()
        for itemset, count in candidate_count.items():
            if count >= min_support:
                current_candidates.add(itemset)
                support_data[itemset] = count

        if current_candidates:
            frequent_itemsets.extend(current_candidates)

    # Додаємо часті 1-елементні множини
    frequent_itemsets.extend(L)

    return frequent_itemsets, support_data, "AIS"