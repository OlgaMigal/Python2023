# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3

def task32():
    # Уж не стала делать ручной ввод. При необходимости могу.
    my_list = [3, 4, 2, 5, 6, 7]
    diapasone = [4, 6]

    index_list = [i for i in range(0, len(my_list)) if diapasone[0]<=my_list[i]<=diapasone[-1]]
    print(*index_list)

task32()