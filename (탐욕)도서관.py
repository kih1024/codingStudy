# https://www.acmicpc.net/problem/1461
# heapq 를 이용해서 plus ,minus 각각 만들어 풀수도 있음

import heapq

n, m = map(int, input().split())

books = list(map(int, input().split()))
left = []
right = []
result = 0
for i in books:
    if i < 0:
        heapq.heappush(left, i)
    else:
        heapq.heappush(right, -i)

largest = max(max(books), -min(books))

while left:
    result += heapq.heappop(left)
    for _ in range(m - 1):
        if left:
            heapq.heappop(left)
while right:
    result += heapq.heappop(right)
    for _ in range(m - 1):
        if right:
            heapq.heappop(right)

print(-2 * result - largest)

