# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.



# def arithProg(number, diff, count):
#     arr = []
#     for i in range(1, count+1):
#         arr.append(number + (i-1)*diff)
#     return arr
# number = int(input('Введите первый элемент: '))
# diff = int(input('Введите длину шага: ')) 
# count = int(input('Введите количество элементов: '))
# print('Арифметическая прогрессия по введенным элементам: ', arithProg(number,diff,count))



# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


import random
number = int(input('Введите длину массива: '))
min_number = int(input('Введите минимальное число: '))
max_number = int(input('Введите максимальное число: '))
list1 = []
for i in range(number+1):
    i = random.randint(1,10)
    list1.append(i)
print(list1)
for i in range(len(list1)):
    if min_number <= list1[i] <= max_number:
        print(f'Число которое входят в диапозон равно {list1[i]}. Индекс числа равен {i}')