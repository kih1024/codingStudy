# https://www.acmicpc.net/problem/2012
n = int(input())
arr = []
result = 0
for _ in range(n):
    temp = int(input())
    arr.append(temp)
arr.sort()

for i in range(n):
    result += abs((i + 1) - arr[i])

print(result)
