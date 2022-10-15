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

from functools import reduce
import random
def digs(num):
    num = random.randint(0,10)
    return num
stripe = [digs(i) for i in range(1, 11)]
print('2.', stripe)
res = reduce(lambda h,l: h+l, stripe)
print('Сумма элементов на нечётных позициях в данном списке =', res)

# Семинар №3
# Задание 3 Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# Старая версия:

# import random
# strip = []
# for i in range(si):
#     num = round(random.uniform(-10.1, 10.1), 2)
#     strip.append(num)
# big = strip[0]
# tin = strip[0]
# print('3.', strip, '\n' 'Разность между максимальным и минимальным значениями данного списка =', end=' ')
# for i in strip:
#     if i%1>=big%1:
#         big=i
#     elif i%1<=tin%1 and i%1!=0:
#         tin=i
# print(big, '-', tin, '=', round((big%1)-(tin%1), 2))

# Новая версия

def digs(num):
    num = round(random.uniform(-10,10), 2)
    return num
res = list(digs(i) for i in range(0, 11))
print('3.', res)
res = list(map(lambda i: i % 1, res))
def mima(res):
    return round(max(res) - min(res), 2)
print(round(max(res), 2), '-', round(min(res), 2), '=', mima(res))

# Семинар №4
# Задание 2 Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# Старая версия:

# num = int(input("2. Введите число: "))
# multi = []
# i = 2
# while i <= num:
#     if num % i == 0:
#         num /= i
#         multi.append(i)
#         i = 2
#     else:
#         i += 1
# print('множители данного числа:', multi)

# Новая версия

dig = 2
num = int(input("4. Введите число: "))
def vide(dig, num):
    if num % dig == 0:
        num = round(num / dig)
        dig = 2
    else:
        dig += 1
    if num % dig == 0:
        return dig, num
    else:
        return dig == '', num == ''
multi = list(vide(dig, num) for dig in range(2, num) if dig<=num)
# multi = list(filter(lambda x: None not in x, multi))
print(multi)