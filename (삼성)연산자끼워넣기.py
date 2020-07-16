from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
# 덧셈 뺄셈 곱셈 나눗셈 의 갯수
idx = list(map(int, input().split()))
op = []
for i in range(len(idx)):
    for j in range(idx[i]):
        op.append(i)
result = []
li = set(permutations(op, n - 1))
for i in li:
    temp = arr[0]
    for j in range(n - 1):
        if i[j] == 0:
            temp = temp + arr[j + 1]
        elif i[j] == 1:
            temp = temp - arr[j + 1]
        elif i[j] == 2:
            temp = temp * arr[j + 1]
        else:
            if temp < 0:
                temp = -temp // arr[j + 1]
                temp = -temp
            else:
                temp = temp // arr[j + 1]
    result.append(temp)
# print(len(set(permutations([1, 2, 3, 3, 5, 5, 7, 7, 9, 10, 11], 11))))
print(max(result))
print(min(result))
