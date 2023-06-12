'''
Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''

# a, d, n = [int(input(f'Введите {x}: ')) for x in ('первый элемент', 'разность', 'количество элементов')]

# progression = [a + d * i for i in range(n)]

# print(f'Элементы арифметической прогрессии: {progression}')

'''
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''

# import random

# n = [random.randint(1, 10) for _ in range(random.randint(8, 15))]
# print(n)
# min_value, max_value = [int(input(f'Введите {_} значение: ')) for _ in ('min', 'max')]

# [print(_, end=' ') for _ in range(len(n)) if min_value <= n[_] <= max_value]


# def divisible_seven(number: str, sign: int) -> int:
#     if len(number) > 3:
#         return sign * int(number[-3:]) + divisible_seven(number[:-3], -1 if sign == 1 else 1)
#     else:
#         return sign * int(number)