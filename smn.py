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
res = digs[0]
# ints = list(i+res for i in range(len(digs), map(int, digs)))
ints = sum(map(int, digs))
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
res = 0
def digs(num):
    num = random.randint(0,10)
    return num
def summa(res):    
    for i in range(len(stripe)):
        if i%2!=0:
            res += stripe[i]
    return res
stripe = [digs(i) for i in range(1, 11)]
sprint = list((x,'|',i) for x,i in enumerate(stripe))
print('2.', sprint)
print('Сумма элементов на нечётных позициях в данном списке =', summa(res))

# Семинар №3
# Задание 3 Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# Старая версия:

# import random
# si = int(input('3.o Задайте длину списка: '))
# strip = []
# for i in range(si):
#     num = round(random.uniform(-10.1, 10.1), 2)
#     strip.append(num)
# big = strip[0]
# tin = strip[0]
# print('3.', strip, '\n' 'Разность между максимальным и минимальным значениями данного списка =', end=' ')
# for i in strip:
#     if i - int(i) >= big - int(big):
#         big = i
#     elif i - int(i) <= tin - int(tin) and i - int(i) != 0:
#         tin = i
# print(big - int(big), '-', tin - int(tin), '=', (big - int(big)) - (tin - int(tin)))

# Новая версия:

def digs(num):
    num = round(random.uniform(-10,10), 2)
    return num
res = list(digs(i) for i in range(0, 11))
print('3.', res)
res2 = list(map(lambda i: round(i - int(i), 2), res))
def mima(res2):
    return max(res2) - min(res2)
print(max(res2), '-', min(res2), '=', round(mima(res2), 2))

# Семинар №4
# Задание 2 Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# Старая версия:

# num = int(input("2.o Введите число: "))
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

# Новая версия:

dig = 2
num = int(input("4. Введите число: "))
def vide(dig, num):
    if num % dig == 0 and dig!=num:
        num = round(num / dig)
        return dig, num
    else:
        dig += 1
    if num % dig == 0:
        return dig == 2
multi = list(filter(lambda x: x != None, list(vide(dig, num) for dig in range(2, num) if dig <= num)))
print(multi)