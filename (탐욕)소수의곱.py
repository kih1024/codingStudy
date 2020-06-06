# https://www.acmicpc.net/problem/2014
import heapq
from copy import deepcopy

k, n = map(int, input().split())
arr = list(map(int, input().split()))
li = deepcopy(arr)

for i in range(n):
    mn = heapq.heappop(li)

    for i in arr:
        heapq.heappush(li, mn * i)
        if mn % i == 0:
            break

print(mn)
# while count < n:
#     mn = heapq.heappop(li)
#     if mn in ck:
#         continue
#     count += 1
#     ck.add(mn)

#     for i in arr:
#         if mn * i < 2 ** 32:
#             heapq.heappush(li, mn * i)

# print(mn)
