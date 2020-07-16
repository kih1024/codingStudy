# di = dict()

# arr = [1, 1, 1, 1]
# arr2 = [2,2,2,2,2]
# print(arr+arr2)

# arr = [[0] * 10 for i in range(10)]


# for i in range(5):
#     for j in range(5):
#         arr[i][j] = 2

# # arr[0:2][0] = arr[7:9][0]
# print(arr[3:9][0])
# for k in arr:
#     print(k)
# d=1
# print([d,'asd'][d!=1])
from copy import deepcopy

s = set()
li = [1, 2, 3]
s = s | set(li)
print(s)
li2 = [23, 4, 5]
s2 = set(li2)
s = s2
s2 = s2 | set([55, 55])
print(s, s2)
