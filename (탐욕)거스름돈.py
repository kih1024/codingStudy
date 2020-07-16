# https://www.acmicpc.net/problem/5585
n = int(input())
result = 0
temp = 1000 - n
for i in [500, 100, 50, 10, 5, 1]:
    result += temp // i
    temp = temp % i
print(result)
