# https://www.acmicpc.net/problem/1092
import sys

input = sys.stdin.readline
n = int(input())
limit = list(map(int, input().split()))

m = int(input())
weight = list(map(int, input().split()))

arr = [False] * m
position = [0] * n

limit.sort(reverse=True)
weight.sort(reverse=True)

count = 0
result = 0
if limit[0] < weight[0]:
    print(-1)
    sys.exit()

while True:
    if count == m:
        break
    for i in range(len(limit)):
        while position[i] < m:
            if arr[position[i]] == False and limit[i] >= weight[position[i]]:
                count += 1
                arr[position[i]] = True
                position[i] += 1
                break
            position[i] += 1
    result += 1

print(result)


# while count != len(weight):
#     for i in range(n):
#         for j in range(start,m):
#             if arr[j] == False and limit[i] >= weight[j]:
#                 arr[j] = True
#                 count += 1
#                 # print(arr)
#                 break
#     result += 1

# # print(arr)
# print(result)

