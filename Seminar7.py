# def f(n):
#     return n**2
#
# def f1(n):
#     return n%2 == 0
#
#
# pre_arr = input().split()
# print(pre_arr)
# pre_arr = list(map(int, pre_arr))
# # # arr = list(map(f, pre_arr))
# # arr = list(map(lambda x: x**2, pre_arr))
# # print(arr)
#
# arr = list(filter(f1, pre_arr))
# print(arr)

# zip
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [11, 22, 33, 44, 55, 66]
#
# arr3 = list(zip(arr1, arr2))
# print(arr3)


# enumerate
# arr = [11, 22, 33, 44, 55, 66]
#
# arr_res = list(enumerate(arr))
# print(arr_res)

# Дан список. Вывести в отдельном списке буквы, а в другом цифры, используя фильтр
# list_1 = ["asd", 1, 2, "gfd"]
#
# list_res_letters = list(filter(lambda x: type(x)==str, list_1))
# print(list_res_letters)
# list_res_numbers = list(filter(lambda x: type(x)==int, list_1))
# print(list_res_numbers)


# Дано вещественное число. Показать сумму его цифр.
# 3.12 = 6

# num = float(input())
# res = list(filter(lambda x: x!='.', str(num)))
# res1 = sum(list(map(int, res)))
# print(res1)

# Дан список целых чисел. Оставить в нём только двузначные числа.
#
# my_list = [1, 55, 3, -26, 685, 999, 7774, 2, 77, 10, 99, 100, 0]
# res = list(filter(lambda x: 9<abs(x)<100, my_list))
# print(res)

У вас есть код, который вы не можете менять(так часто бывает, когда код в
глубине программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.


```python
transformation = lambda x: x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformed_values = list(map(transformation, values))
if values == transformed_values:
	print('ok')
else:
	print('fail')
```
