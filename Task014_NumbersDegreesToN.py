# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.


N = int(input("Введите число N: "))
magicNumber = 2

resultList = [magicNumber**i for i in range (1, N) if magicNumber**i<=N]
print(resultList)