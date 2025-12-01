def best_diagnosis_by_wald(rules):
    """
    rules — список правил, де кожне правило містить:
    - support
    - confidence
    - lift
    Повертає правило, яке є найкращим за критерієм Вальда.
    """

    if not rules:
        return None

    best_rule = None
    best_wald_value = float('-inf')

    for rule in rules:
        # Найгірший показник для правила (min -> песимістичний сценарій)
        worst_metric = min(rule["support"], rule["confidence"], rule["lift"])

        # Вальд: вибрати максимальний з цих мінімумів
        if worst_metric > best_wald_value:
            best_wald_value = worst_metric
            best_rule = rule

    return best_rule
