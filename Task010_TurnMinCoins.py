# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монет: "))
obverse = 0
reverse = 0
for i in range(1,n+1):
    temp = int(input(f"Введите 1 (орёл) или 0 (решка) для монетки №{i}: "))
    if temp == 1:
        obverse +=1
    elif temp == 0:
        reverse +=1
    else:
        print("Эй, уберите со стола монетку Пить-Тоже Пить!!!")
if obverse>reverse:
    print (f"Минимальное число переворотов = {reverse}")
else:
    print(f"Минимальное число переворотов = {obverse}")