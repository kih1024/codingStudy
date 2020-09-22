import sys

input = sys.stdin.readline

N = int(input())
m = int(input())
graph = [[1e9] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] != 1e9:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == 1e9:
            graph[i][j] = 0
        print(graph[i][j], end=" ")
    print()
