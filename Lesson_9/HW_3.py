# 3) Считайте строку, содержащую натуральное число - число пончиков
# Напишите функцию, принимающую на вход число пончиков, а возвращающую строку:
# •	"Всего пончиков: <число>", если пончиков не больше 9
# •	"Всего пончиков: много", если пончиков больше 9
# Выведите на печать результат работы функции для считанного числа пончиков.



donut_amount = int(input())

def func (donut):
    if donut > 0: 
        if donut < 10 :
          return f"Всего пончиков: {donut} "
        elif donut > 9:
         return "Всего пончиков: Много"
    else:
        "Введите положительное число"

print(func(donut_amount))
