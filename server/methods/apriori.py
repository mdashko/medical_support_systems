from collections import defaultdict

def get_frequent_itemsets_apriori(transactions, min_support=2):
    item_count = defaultdict(int)

    # Підрахунок частоти 1-елементних множин
    for transaction in transactions:
        for item in transaction:
            item_count[frozenset([item])] += 1

    # Часті 1-елементні множини
    L1 = {item for item, count in item_count.items() if count >= min_support}
    support_data = {item: count for item, count in item_count.items() if count >= min_support}

    L = [L1]  # Список частих наборів
    k = 2

    while True:
        prev_L = list(L[-1])  # попередній набір частих елементів
        candidate_k = set()

        # Генерація кандидатів для k-елементних множин
        for i in range(len(prev_L)):
            for j in range(i + 1, len(prev_L)):
                union_set = prev_L[i].union(prev_L[j])
                if len(union_set) == k:
                    candidate_k.add(union_set)

        # Підрахунок підтримки для кандидатів
        candidate_count = defaultdict(int)
        for transaction in transactions:
            trans_set = set(transaction)
            for candidate in candidate_k:
                if candidate.issubset(trans_set):
                    candidate_count[candidate] += 1

        # Зберігаємо часті k-набори
        Lk = {itemset for itemset, count in candidate_count.items() if count >= min_support}
        if not Lk:
            break

        support_data.update({item: count for item, count in candidate_count.items() if count >= min_support})
        L.append(Lk)
        k += 1

    return L, support_data, "Apriori"