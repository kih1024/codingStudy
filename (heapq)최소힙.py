import heapq
import sys

heap = []
n = int(sys.stdin.readline())
for i in range(n):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if len(heap) == 0:
            print(0)
            continue
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, temp)