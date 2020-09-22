import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [1e9] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0
while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

max_value = 0
max_idx = 0
result = []
for i in range(2, len(distance)):
    if max_value < distance[i]:
        max_value = distance[i]
        max_idx = i
        result = [max_idx]
    elif max_value == distance[i]:
        result.append(i)

print(max_idx, max_value, len(result))

# 입력 예제
# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2