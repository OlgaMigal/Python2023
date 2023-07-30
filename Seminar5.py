# 1. Последовательностью Фибоначчи называется последовательность
# чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи
# n = 5
# def fibonacci(n):
#     if n in [1, 2]:
#            return 1
#     return fibonacci(n-1)+fibonacci(n-2)
# list_1 = []
# for i in range (1, n+1):
#     list_1.append(fibonacci(i))
# print(list_1)
# print(fibonacci(n))



# Хакер Василий получил доступ к классному журналу и хочет
# заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.


# 1 2 3 4 5 5 5 5
# 1 2 3 4 1 1 1 1
# my_list = [1, 2, 3, 4, 5, 5, 5, 5]
#
# def min_max(my_list):
#     min = max = my_list[0]
#     for i in my_list:
#         if i>max:
#             max=i
#         if i<min:
#             min = i
#     return (min, max)
#
# min, max = min_max(my_list)
#
# def change_min_max(my_list, min, max):
#     for i in range(len(my_list)):
#         if my_list[i]==max:
#             my_list[i]=min
#     return my_list
#
# print (change_min_max(my_list, min, max))



# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Возвращает Yes или No
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*

# n = int(input("Введите число: "))
# def simple_num(n):
#     for i in range(2,n//2):
#         if n%i != 0:
#             return(print(f'Число {n} простое'))
#         else:
#             return(print(f"Число {n} не является простым"))


# simple_num(n)


# Вариант2:
# def CheckingProstNum (num):
#     for i in range(2, int(num**0.5)+1): #единицу добавляем для получения следующего целого числа после квадратного корня
#         if num % i == 0:
#             return ("Число не простое")
#     return ("Число простое") #число простое по умолчанию!
#
# n = int(input("Введите число N для проверки простоты: "))
# print(CheckingProstNum(n))



# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
#
# 1
# 2
# 3
# 4
# 5
#
# func(5)
#
#
# # 5 4 3 2 1
# def func(n):
#     if n == 0:
#         return ""
#     num = input('введите элемент ')
#     return func(n - 1) + f' {num}'
#
# print(func(5))


def sum(a, b):
    if b == 0:
        return(a)
    else:
        return(sum(a + 1, b - 1))
print(sum(5, 8))