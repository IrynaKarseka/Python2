# Задача 30:
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: 
#                                   an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# list_1 = list()

# a1 = int(input('Введите первый элемент арифметической прогрессии '))
# d = int(input('Введите разность арифметической прогрессии '))
# count = int(input('Введите количество элементов арифметической прогрессии '))

# for i in range(count):
#     if i == 0:
#         list_1.append(a1)
#     else:
#         n = a1 + i * d
#         list_1.append(n)

# print(list_1)

# Задача 32: 
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]   

# index_start = 5
# index_final = 10

# list_2 = []

# for i in range(len(list_1)):
#     if index_start <= list_1[i] and list_1[i] <= index_final:
#         list_2.append(i)

# print(list_2)