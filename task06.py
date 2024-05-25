def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories']/x[1]['cost'], reverse=True)
    selected_items = {}
    total_cost = 0
    total_calories = 0

    for item, values in sorted_items:
        if total_cost + values['cost'] <= budget:
            selected_items[item] = values
            total_cost += values['cost']
            total_calories += values['calories']

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    for i, (item, values) in enumerate(items.items(), 1):
        for j in range(1, budget + 1):
            if values['cost'] > j:
                dp_table[i][j] = dp_table[i-1][j]
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i-1][j-values['cost']] + values['calories'])

    selected_items = {}
    total_calories = dp_table[len(items)][budget]
    remaining_budget = budget

    for i in range(len(items), 0, -1):
        if dp_table[i][remaining_budget] != dp_table[i-1][remaining_budget]:
            item = list(items.keys())[i-1]
            selected_items[item] = items[item]
            remaining_budget -= items[item]['cost']

    return selected_items, total_calories

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Виклик функцій для жадібного алгоритму та динамічного програмування
greedy_result = greedy_algorithm(items, budget)
dynamic_result = dynamic_programming(items, budget)

print("Greedy Algorithm Result:")
print(greedy_result)

print("\nDynamic Programming Result:")
print(dynamic_result)
