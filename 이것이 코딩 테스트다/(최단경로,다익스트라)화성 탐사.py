import heapq
import sys

input = sys.stdin.readline

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
for _ in range(int(input())):
    N = int(input())
    energy = [list(map(int, input().split())) for _ in range(N)]
    distance = [1e9] * (N ** 2)
    graph = [[] for _ in range(N ** 2)]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                r, c = i + dy[k], j + dx[k]
                if r < 0 or r >= N or c < 0 or c >= N:
                    continue
                # graph[i] = [(목적지,가는데걸린비용)]
                graph[i * N + j].append((r * N + c, energy[r][c]))

    q = []
    heapq.heappush(q, (energy[0][0], 0))
    distance[0] = energy[0][0]

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    print(distance[(N ** 2) - 1])

# 입력 예제
# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
