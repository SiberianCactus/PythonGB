# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1



n = int(input('Введите количество элементов: '))

array = [i+1 for i in range(n)]
print(array)

x = int(input('Введите требуемое число: '))
number_to_find = 0
for i in array:
    if i == x:
        number_to_find += 1
        print(number_to_find)