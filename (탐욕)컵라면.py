# https://www.acmicpc.net/problem/1781
import sys
import heapq

n = int(input())
arr = []
heap = []
for _ in range(n):
    dead, cup = map(int, input().split(" "))
    arr.append((dead, cup))

arr.sort()

for i in range(len(arr)):
    heapq.heappush(heap, arr[i][1])
    if arr[i][0] < len(heap):
        heapq.heappop(heap)

print(sum(heap))


# import heapq

# N = int(input())
# heap = []
# array = [[] for _ in range(N + 1)]
# for _ in range(N):
#     deadline, cupramen = map(int, input().split())
#     array[deadline].append(cupramen)

# for i in range(N + 1):
#     if not array[i]:
#         continue
#     array[i].sort()
#     for j in array[i]:
#         if i == len(heap):
#             heapq.heappop(heap)
#         heapq.heappush(heap, j)
#         print(heap)
# print(heap)
# print(sum(heap))

