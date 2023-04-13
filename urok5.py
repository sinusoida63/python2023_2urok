# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# Пример:

# A = 3; B = 5 -> 243 (3⁵) A = 2; B = 3 -> 8



# def degreeNumbers(a, b):
#     if b == 0:
#         return 1
#     return a * degreeNumbers(a, b - 1)
# number = int(input('Введите число: '))
# degree = int(input('Введите степень: '))
# print(f'{number}^{degree} = {degreeNumbers(number, degree)}')



# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Пример:

# 2 2 4


def recSum(a, b):
    if b == 0:
        return a
    return 1 + recSum(a, b - 1)
number1 = int(input('Введите число: '))
number2 = int(input('Введите число: '))
print(f'{number1} + {number2} = {recSum(number1, number2)}')