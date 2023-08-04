def f(n):
    return n**2

def f1(n):
    return n%2 == 0


pre_arr = input().split()
print(pre_arr)
pre_arr = list(map(int, pre_arr))
# # arr = list(map(f, pre_arr))
# arr = list(map(lambda x: x**2, pre_arr))
# print(arr)

arr = list(filter(f1, pre_arr))
print(arr)