# 4) Считайте строку (используйте input()), содержащую 1 натуральное число n
# Найдите сумму всех чисел от 0 до n, включительно, которые делятся на 5 без остатка, но на 3 делятся с остатком.

number = int(input())

def sum(number):
    sum1 = 0
    for i in range(number+1):
        if i%5==0 and i%3 !=0 :
            sum1 +=i
    return sum1
    

print(sum(number))