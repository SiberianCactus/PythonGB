# 2) Напишите функцию front_x(words), которая на вход принимает список строк и возвращает отсортированный по правилам:
# 1	слова, начинающиеся с символа "x", идут первыми
# 2	в лексикографическом порядке.
# Важно! Список может содержать пустые строки - "" - их нельзя выкидывать и при их обработке функция не должна "падать".


# Примечание. Пример вывода дан для words = ['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']
# В данной задаче не требуется осуществлять вывод - проверка производится для разных списков!


def func(words):
    x_first = [word for word in words if len(word) != 0 and word[0] == 'x']
    x_not_first = [word for word in words if len(word) == 0 or word[0] != 'x']
    return sorted(x_first) + sorted(x_not_first)


print(func(['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']))