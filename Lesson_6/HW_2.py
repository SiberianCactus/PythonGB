# Задача 32: Определить индексы элементов массива (списка), 
# # значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


first_number = int(input("Введите начало диапозона: "))
second_number = int(input("Введите конец диапозона: "))
array = [1,13,44,23,86,100]

def func(first,second):
    new_array = [i for i in range(len(array)) if array[i] <= second and array[i] >= first]
    return new_array

print("Индексы чисел массива, входящие в ваш диапозон: ", func(first_number, second_number))