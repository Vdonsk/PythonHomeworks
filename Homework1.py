'''
Задача 2: Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
'''

# num = int(input('Введите трехзначное число: '))

# a = num // 100
# b = num % 100 // 10
# c = num % 10

# sum = a + b + c
# print(f'Сумма цифр трехзначного числа: {sum}')

'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Пример:
6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
'''

# c = int(input('Общее количество журавликов: '))

# s = c / 6
# p = s
# k = (s + p) * 2

# print(f'Количество журавликов сделаных детьми: Сережа: {int(s)} Катя: {int(k)} Петя: {int(p)} ')

'''
Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no
'''

# b = str(input('Введите шестизначный номер билета: '))

# sum1 = int(b[0]) + int(b[1]) + int(b[2])
# sum2 = int(b[3]) + int(b[4]) + int(b[5])

# if sum1 == sum2:
#     print('YES')
# else:
#     print('NO')

'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
Пример:
3 2 4 -> yes
3 2 1 -> no
'''

# n = int(input('n: '))
# m = int(input('m: '))
# k = int(input('k: '))

# if k%n == 0 and k/n < m or k%m == 0 and k/m < n:
#     print('YES')
# else:
#     print('NO')