import random

# Функція для симуляції кидків двох кубиків та обчислення суми
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

# Створення словника для збереження кількості кожної суми
results = {i: 0 for i in range(2, 13)}

# Кількість ітерацій для симуляції
num_iterations = 100000

# Виконання симуляції
for _ in range(num_iterations):
    total = roll_dice()
    results[total] += 1

# Обчислення ймовірностей
probabilities = {key: value / num_iterations * 100 for key, value in results.items()}

# Виведення результатів
print("Сума\tІмовірність")
for key, value in probabilities.items():
    print(f"{key}\t{value:.2f}% ({results[key]}/{num_iterations})")


#Сума	Імовірність
#2	2.80% (2803/100000)
#3	5.56% (5557/100000)
#4	8.35% (8351/100000)
#5	11.18% (11178/100000)
#6	13.83% (13834/100000)
#7	16.51% (16508/100000)
#8	14.01% (14009/100000)
#9	11.18% (11176/100000)
#10	8.31% (8309/100000)
#11	5.47% (5470/100000)
#12	2.80% (2805/100000)
