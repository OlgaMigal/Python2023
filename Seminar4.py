# 25. Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
#
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


# str = input("Введите строку: ").split()
# result_str = ""
# dict_str = {}
#
#
# for i in str:
#     if i not in dict_str:
#         result_str += f'{i} '
#     else:
#         result_str += f"{i}_{dict_str[i]} "
#     dict_str[i] = dict_str.get(i, 0)+1
#
# print(result_str)


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# str = input("Введите строку: ")
# str = str.upper()
# str = str.split()
# result_str = ""
# dict_str = {}
# counter = 0
#
# for i in str:
#     if i not in dict_str:
#         counter += 1
#         result_str += f'{i} '
#         dict_str[i] = None
# print(f'{counter} разных слов: {result_str}')


# print(len(set(input("Введите строку: ").lower().split())))



# Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента  последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность)

my_list = [5, 6, 8, 2, 505, 64, 0, 14, 666]
max=0
for i in my_list:
    if i!=0:
        if i>max:
            max = i
    else: break
print(max)
