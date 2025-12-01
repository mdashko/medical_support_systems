from generate_rules import *
from methods.apriori import get_frequent_itemsets_apriori
from methods.dhp import get_frequent_itemsets_dhp
from methods.partition import get_frequent_itemsets_partition
from methods.ais import get_frequent_itemsets_ais
from generate_rules_ais import *
from wald import best_diagnosis_by_wald
from settings import CSV_FILE

def convert_format(algorithmsName, matching, selected, frequent_itemsets, association_rules, wald_result):
    res = {
        "algorithmsName": algorithmsName,
        "requested_symptoms": selected,
        "matching_count": len(matching),
        "matching_rows": matching,
        "transactions_count": len(matching),
        "frequent_itemsets": [list(map(list, level)) for level in frequent_itemsets],
        "association_rules": association_rules,
        "wald": wald_result
    }
     
    return {
        "res": res,
		"algorithmsName": res["algorithmsName"],
		"wald": res["wald"] if res["wald"] is not None else "Немає"
	}

# Алгоритми та їх генератори правил
ALGORITHMS = [
    ("apriori", get_frequent_itemsets_apriori, generate_rules_apriori),
    ("dhp", get_frequent_itemsets_dhp, generate_rules_dhp),
    ("partition", get_frequent_itemsets_partition, generate_rules_partition),
    ("ais", get_frequent_itemsets_ais, generate_rules_ais),
]


def combine_all_rules(matching, selected):

    results = []

    for name, algo_func, rule_generator in ALGORITHMS:
        # Отримуємо часті набори
        frequent_itemsets, support_data, algorithmsName = algo_func(
            matching
        )

        # Генеруємо правила
        association_rules = rule_generator(
            frequent_itemsets, support_data, matching
        )

        # Критерій Вальда
        wald_result = best_diagnosis_by_wald(association_rules)

        # Додаємо у результат
        results.append(
            convert_format(
                algorithmsName,
                matching,
                selected,
                frequent_itemsets,
                association_rules,
                wald_result
            )
        )

    return results
