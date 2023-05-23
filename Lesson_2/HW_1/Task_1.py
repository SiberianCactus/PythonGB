
import random
"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
 Выведите минимальное количество монет, которые нужно перевернуть
"""

side = ["tail", "head"]
count = int(input("Введите количество монет: "))

Coins = []

while len(Coins) < count:
    Coins.append(random.choice(side))

head,tail = 0,0

for i in range(len(Coins)):
    if Coins[i] == "head":
        head +=1
    elif Coins[i] == "tail":
        tail +=1
    i+=1

print(Coins)
print(f"Орел: {head}")
print(f"Решка: {tail}")


if head < tail:
    print(f"Нужно перевернуть {head} монет")
elif head == tail:
    print(f"Нужно перевернуть {count/2} монет с любой стороной")
elif head == 0 or tail == 0:
     print("Все монеты повернуты одной стороной, поворачивать ничего не нужно")
else: 
     print(f"Нужно перевернуть {tail} монет")
