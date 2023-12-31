# 25. Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
#
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


str = input("Введите строку: ").split()
result_str = ""
dict_str = {}


for i in str:
    if i not in dict_str:
        result_str += f'{i} '
    else:
        result_str += f"{i}_{dict_str[i]} "
    dict_str[i] = dict_str.get(i, 0)+1

print(result_str)