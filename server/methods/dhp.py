from collections import defaultdict
from itertools import combinations

def get_frequent_itemsets_dhp(transactions, min_support=2, bucket_size=1000):
    """
    DHP (Direct Hashing and Pruning)
    Повертає (L, support_data, "DHP") у форматі, сумісному з Apriori.
    """

    # ---------- 1) Часті 1-елементні множини ----------
    item_count = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_count[frozenset([item])] += 1

    L1 = {item for item, count in item_count.items() if count >= min_support}
    support_data = {item: count for item, count in item_count.items() if count >= min_support}

    L = [L1]
    k = 2

    # ---------- Основний цикл DHP ----------
    while True:
        prev_L = list(L[-1])
        candidate_k = set()

        # ---------- 2) Генерація кандидатів (як у Apriori) ----------
        for i in range(len(prev_L)):
            for j in range(i + 1, len(prev_L)):
                union_set = prev_L[i].union(prev_L[j])
                if len(union_set) == k:
                    candidate_k.add(union_set)

        if not candidate_k:
            break

        # ---------- 3) Хеш-таблиця для k-піднаборів ----------
        buckets = defaultdict(int)

        for transaction in transactions:
            t = sorted(set(transaction))
            if len(t) >= k:
                for comb in combinations(t, k):
                    # Хеш-функція як у класичному DHP
                    h = 0
                    for item in comb:
                        h = (h * 131 + hash(item)) & 0x7FFFFFFF
                    bucket = h % bucket_size
                    buckets[bucket] += 1

        # ---------- 4) Відсіювання кандидатів за bucket count ----------
        filtered_candidates = set()
        for cand in candidate_k:
            h = 0
            for item in sorted(cand):
                h = (h * 131 + hash(item)) & 0x7FFFFFFF
            bucket = h % bucket_size

            if buckets[bucket] >= min_support:
                filtered_candidates.add(cand)

        if not filtered_candidates:
            break

        # ---------- 5) Підрахунок підтримки для кандидатів ----------
        candidate_count = defaultdict(int)
        for transaction in transactions:
            trans_set = set(transaction)
            for candidate in filtered_candidates:
                if candidate.issubset(trans_set):
                    candidate_count[candidate] += 1

        # ---------- 6) Зберігаємо часті набори ----------
        Lk = {itemset for itemset, count in candidate_count.items() if count >= min_support}
        if not Lk:
            break

        support_data.update({item: count for item, count in candidate_count.items() if count >= min_support})
        L.append(Lk)
        k += 1

    return L, support_data, "DHP"
