# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

from random import randint
import math

def task016():
    k = 2
    list_1 = list_creation()
    minimum = find_close_element(list_1, k)
    print(f'В списке {list_1} самый близкий к {k} элемент это {minimum}')


def list_creation():
    length = int(input('Введите длину списка: '))
    my_list = []
    for _ in range(length):
        my_list.append(randint(1, 9))
    return my_list


def find_close_element(my_list, element):
    min = my_list[0]
    temp = my_list[0]-element
    for i in my_list:
        if i-element<=abs(temp):
            min = i
    return min


task016()