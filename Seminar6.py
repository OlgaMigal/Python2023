# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# print(i, end=" ")


# def task039():
#     m = int(input("Введите длину списка m: "))
#     n = int(input("Введите длину списка n: "))
#     list_m = list_creator(m)
#     list_n =list_creator(n)
#     res_list = set_from_list(list_m, list_n)
#     print(*res_list)
#
# def list_creator(x):
#     my_list = []
#     for i in range(0, x):
#         my_list.append(int(input(f"Введите элемент списка из {x} элементов: ")))
#     return my_list
#
# def set_from_list(list_m, list_n):
#     my_list = [list_m[i] for i in range(len(list_m)) if list_m[i] not in list_n]
#     return my_list
#
# task039()


# Дан массив, состоящий из целых чисел. Напишите программу,
# которая в данном массиве определит количество элементов, у которых два соседних
# и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество
# элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.


# def task41():
#     list_new = [200, 100, 6, 2, 54, 1, 5, 23]
#     print(find_between_less_elements(list_new))
#
# def find_between_less_elements(my_list):
#     count = 0
#     for i in range(1,len(my_list)-1):
#         if my_list[i-1]<my_list[i]>my_list[i+1]:
#             count +=1
#     return count
#
# task41()

#от Ивана Логина
# n = int(input('Введите кол-во элементов множества -> '))
# arr = [input('Введите элемент массива -> ') for i in range(0, n)]
# res = [1 for i in range(0,len(arr)) if arr[i - 2] < arr[i - 1] and arr[i] < arr[i - 1]]
# print(sum(res))

#  Задача No43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
# 1 1 1 1
# (n-1)! = 1*2*3
#
#
# def task043():
#     l = int(input("Введите длину списка: "))
#     list_m = list_creator(l)
#
#
# def list_creator(x):
#     my_list = []
#     for i in range(0, x):
#         my_list.append(int(input(f"Введите элемент списка из {x} элементов: ")))
#     return my_list
#
0#
# def task043()