# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.


from random import randint

def task015():
    k = 2
    list_1 = list_creation()
    count = list_counter(list_1, k)
    print(f'{k} в списке {list_1} встречается {count} раз(а)')


def list_creation():
    length = int(input('Введите длину списка: '))
    my_list = []
    for _ in range(length):
        my_list.append(randint(1, 9))
    return my_list


def list_counter(my_list, element):
    res = 0
    for i in my_list:
        if i==element:
            res +=1
    return res


task015()