def add_person(person):
    data = open('phone_book/Dict.txt', 'a', encoding='utf-8')
    data.write(person)
    data.write('\n')
    data.close()

def show_all():
    data = open ('phone_book/Dict.txt', 'r', encoding ='utf-8')
    for line in data:
        print(line[:-1])
    data.close()

def search_element(name):
    with open ('phone_book/Dict.txt', 'r', encoding ='utf-8') as data:
        for line in data:
            if name in line:
                print(line[:-1])


# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def change_element(name):
    with open ('phone_book/Dict.txt', 'r+', encoding ='utf-8') as data:
        new_data=data.readlines()
        with open('phone_book/Dict.txt', 'w+', encoding='utf-8') as data:

            for line in new_data:
                if name in line:
                    data.write(input('Введите новые данные: '))
                    data.write('\n')
                else:
                    data.write(line)


def del_element(name):
    with open('phone_book/Dict.txt', 'r', encoding='utf-8') as data:
        new_data = data.readlines()
    with open('phone_book/Dict.txt', 'w+', encoding='utf-8') as data:
        for line in new_data:
            if name not in line:
                data.write(line)
