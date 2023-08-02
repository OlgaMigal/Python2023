

# my_list = [1, 2, 3, 5, 8, 15, 23, 38]
# answer = [(i, i**2) for i in my_list if i%2==0]
# print(answer)

# вариант №2
# res = list()
#
# for i in my_list:
#     if i%2 == 0:
#         res.append((i, i**2))
# print(res)

 # то же самое через lambda:
def select(f, col):
     return [f(x) for x in col]

def where(f, col):
     return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x ** 2), res))
print(res)
