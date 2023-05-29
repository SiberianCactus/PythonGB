# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


n = int(input('Введите количество элементов: '))
array = []
for i in range(n):
    array.append(int(input()))
print(array)

array.sort()
# print(array)

x = int(input('Введите требуемое число: '))

for i in range(len(array)):
    if x > array[n-1]:
        print(array[n-1])
        break
    elif x < array[0]:
        print(array[0])
        break
    elif x == array[i]:
        print(array[i])
    elif x > array[i] and x < array[i+1]:
            if (array[i] + array[i+1]) /2 == x:
             print(f"Нужное число находится между числами {array[i]} и {array[i+1]}")
             break
            elif (array[i] + array[i+1]) /2 < x:
                    print(array[i+1])
                    break
            else:
                    print(array[i])
                    break







