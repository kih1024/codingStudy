import sys
from collections import deque

def bfs(r, c):
    dq = deque([(r, c)])
    edges = []
    while dq:
        f, s = dq.popleft()
        if not visited[f][s]:
            isEdge = False
            visited[f][s] = True
            for i in range(4):
                y = f + dy[i]
                x = s + dx[i]

                if y >= N or y < 0 or x >= N or x < 0:
                    continue
                if arr[y][x] == 0:
                    isEdge = True

                if not visited[y][x] and arr[y][x] == 1:
                    dq.append((y, x))
            if isEdge:
                edges.append((f, s))
    return edges


def get_distance(f, s):
    global answer
    for i in f:
        for j in s:
            answer = min(abs(i[0] - j[0]) + abs(i[1] - j[1]) - 1, answer)


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
answer = 1e9
island = []
visited = [[False] * N for _ in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] == 1:
            island.append(bfs(i, j))

for i in range(len(island) - 1):
    for j in range(i + 1, len(island)):
        get_distance(island[i], island[j])

print(answer)

