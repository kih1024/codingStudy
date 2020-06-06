# https://www.acmicpc.net/problem/2437

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# 당장 만들수 있는 최대
posible = 0

for i in arr:
    if i <= posible + 1:
        posible += i
    else:
        break

print(posible + 1)
