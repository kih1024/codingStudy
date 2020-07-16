# https://www.acmicpc.net/problem/2212
import sys
import heapq

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()
distance = []
if k >= n:
    print(0)
    sys.exit()

for i in range(n - 1):
    heapq.heappush(distance, -(arr[i + 1] - arr[i]))

for _ in range(k - 1):
    heapq.heappop(distance)

print(-sum(distance))

