# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

from random import randint
import math

def task016():
    k = 22
    list_1 = list_creation()
    minimum = find_max_close_element(list_1, k)
    print(f'В списке {list_1} максимально близким к числу {k} элементом является {minimum}')


def list_creation():
    length = int(input('Введите длину списка: '))
    my_list = []
    for _ in range(length):
        my_list.append(randint(1, 99))
    return my_list


def find_max_close_element(my_list, element):
    temp = my_list[0]-element
    res = my_list[0]
    for i in my_list:
        if abs(i-element)<abs(temp):
            temp = i-element
            res = i
    return res


task016()