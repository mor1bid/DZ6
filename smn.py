# Семинар №2 
# Задание 1 Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

# Старая версия:

# si = int(input('1. Задайте длину списка: '))
# ray = []
# res = 0
# print('Введите', si, 'элемента(-ов) списка:')
# for i in range(si):
#     num = int(input())
#     ray.append(num)
# print(ray)
# for i in range(si):
#     if i%2!=0:
#         res += ray[i]
# print('Сумма элементов на нечётных позициях в данном списке =', res)

# Новая версия:

num = input('1. Введите число: ')
digs = list(filter(lambda x: x.isdigit(), num))
ints = sum(map(int, digs))
res = 0
print('Сумма цифр в числе', num, '=', ints)

# Семинар №3
# Задание 1 Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

# Старая версия:

# si = int(input('1. Задайте длину списка: '))
# ray = []
# res = 0
# print('Введите', si, 'элемента(-ов) списка:')
# for i in range(si):
#     num = int(input())
#     ray.append(num)
# print(ray)
# for i in range(si):
#     if i%2!=0:
#         res += ray[i]
# print('Сумма элементов на нечётных позициях в данном списке =', res)

# Новая версия:

import random
def digs(num):
    num = random.randint(0,10)
    return num
stripe = [digs(i) for i in range(1, 11)]
print('2.', stripe)
res = list(map(int, (i for i in range(len(stripe)) if i%2!=0)))
# for i in range(len(stripe)):
#     if i%2!=0:
#         res+=stripe[i]
# print('Сумма элементов на нечётных позициях в данном списке =', res)
print(res)

# Семинар №3
# Задание 2 Напишите программу, которая найдёт 
# произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.

# Старая версия:

# i2 = 0
# ar = []
# print('2. Произведение пар элементов в данном списке =', end=' ')
# for i in range(si):
#     if i<si/2:
#         i2-=1
#         res= ray[i]*ray[i2]
#         ar.append(res)
# print(ar)

# Новая версия

print('3. Произведение пар элементов в данном списке =', end=' ')
res1 = [x for x in res(int(len(res)/2))]
res2 = [x for x in range(int(len(res)/2), len(res))]
print(res1)
print(res2)
