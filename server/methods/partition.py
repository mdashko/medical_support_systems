def count_itemsets(transactions, itemsets):
    counts = {}
    for itemset in itemsets:
        counts[itemset] = 0
        for transaction in transactions:
            if itemset.issubset(transaction):
                counts[itemset] += 1
    return counts

# Функція для генерації кандидатів k-го рівня
def generate_candidates(prev_frequent_itemsets, k):
    candidates = set()
    prev_itemsets = list(prev_frequent_itemsets)
    for i in range(len(prev_itemsets)):
        for j in range(i + 1, len(prev_itemsets)):
            union_set = prev_itemsets[i].union(prev_itemsets[j])
            if len(union_set) == k:
                candidates.add(union_set)
    return candidates

# Функція Partition для пошуку частих наборів
def get_frequent_itemsets_partition(transactions, min_support=3):
    # Крок 1: Пошук частих 1-елементних наборів
    item_count = {}
    for transaction in transactions:
        for item in transaction:
            key = frozenset([item])
            if key not in item_count:
                item_count[key] = 0
            item_count[key] += 1

    # Зберігаємо часті 1-набори
    L1 = {itemset for itemset, count in item_count.items() if count >= min_support}
    all_frequent_itemsets = [L1]
    support_data = {itemset: count for itemset, count in item_count.items() if count >= min_support}
    k = 2

    # Крок 2: Розбиваємо транзакції на блоки та шукаємо часті набори в кожному блоці
    block_size = max(1, len(transactions) // 2)
    blocks = [transactions[i:i+block_size] for i in range(0, len(transactions), block_size)]

    while True:
        candidates = generate_candidates(all_frequent_itemsets[-1], k)

        if not candidates:
            break

        # Підрахунок у кожному блоці
        global_counts = {}
        for block in blocks:
            block_counts = count_itemsets(block, candidates)
            for itemset, count in block_counts.items():
                if itemset not in global_counts:
                    global_counts[itemset] = 0
                global_counts[itemset] += count

        # Вибираємо часті набори
        frequent_itemsets_k = {itemset for itemset, count in global_counts.items() if count >= min_support}
        if not frequent_itemsets_k:
            break

        all_frequent_itemsets.append(frequent_itemsets_k)
        support_data.update({itemset: count for itemset, count in global_counts.items() if count >= min_support})

        k += 1

    return all_frequent_itemsets, support_data, "Partition"