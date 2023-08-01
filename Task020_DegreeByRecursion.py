# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
#
# Функция не должна ничего выводить, только возвращать значение.


def task020():
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    print(recursion_degree(a,b))

def recursion_degree(m, n):
    if n == 0:
        return 1
    return(recursion_degree(m, n-1)*m)

task020()