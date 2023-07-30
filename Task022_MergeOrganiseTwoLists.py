# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def task022():
    n = int(input("Введите длину списка n: "))
    m = int(input("Введите длину списка m: "))
    list_n = list_creator(n)
    list_m =list_creator(m)
    # print(*list_n)
    # print(*list_m)

    set_1 = set_from_list(list_n)
    set_2 = set_from_list(list_m)
    set_res = set_1.intersection(set_2)
    print(*set_res)

def list_creator(x):
    my_list = []
    for i in range(0, x):
        my_list.append(int(input(f"Введите элемент списка из {x} элементов: ")))
    return my_list

def set_from_list(my_list):
    my_set = set()
    for i in range(len(my_list)):
        my_set.add(my_list[i])
    return my_set

task022()