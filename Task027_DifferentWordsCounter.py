# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

str = input("Введите строку: ")
str = str.upper()
str = str.split()
result_str = ""
dict_str = {}
counter = 0

for i in str:
    if i not in dict_str:
        counter += 1
        result_str += f'{i} '
        dict_str[i] = None
print(f'{counter} разных слов: {result_str}')
