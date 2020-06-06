import heapq
import sys

# 작은거 부터 더해 나간다.
# 새로 더해진것을 추가해야 하므로 힙을 이용
# 정렬은 nlon 이고 추가시 밀리는것 때문에 비효율
# 힙 자료구조는 최대 or 최소를 찾는 logn 시간 걸림

heap = []
total = 0
n = int(sys.stdin.readline())

for i in range(n):
    temp = int(sys.stdin.readline())
    heapq.heappush(heap, temp)

while len(heap) > 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    temp = first + second
    total += temp
    heapq.heappush(heap, temp)

print(total)
