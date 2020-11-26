# ДЗ - Сравнение строк
# Написать функцию, которая принимает на вход две строки
# Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
# Если строки одинаковые, вернуть 1
# Если строки разные и первая длиннее, вернуть 2
# Если строки разные и вторая строка 'learn', возвращает 3
# Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты

print("string compare")

def compare_strings(str1, str2):
    if not (isinstance(str1, str) and isinstance(str2, str)):
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str2 == 'learn':
        return 3
    print(f"unhandled comparison condition for strings '{str1}', '{str2}'!")
    return -1

print(compare_strings(1,2))
print(compare_strings('0', 1))
print(compare_strings(-2.5, '3'))
print(compare_strings('1', '2'))
print(compare_strings('2', '2'))
print(compare_strings('apples', 'apples'))
print(compare_strings('apples', 'oranges'))
print(compare_strings('I am here to', 'learn'))
print(compare_strings('learn', 'I am here to'))
print(compare_strings('learn1', 'learn 2'))
print(compare_strings(None, None))
print(compare_strings('', ''))
print(compare_strings('  ', '  '))
print(compare_strings('', '  '))
print(compare_strings('', None))
print(compare_strings("'", 0))
