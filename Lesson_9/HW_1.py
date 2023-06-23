# 1)  Считайте строку, содержащую произвольное количество целых чисел и найдите их сумму при помощи функции sum().

def sum(num):
    sum1 = 0
    number_array = [int(i) for i in str(num)]
    for i in range(len(number_array)):
        sum1 += number_array[i]
    print(sum1)

number = int(input())
sum(number)
