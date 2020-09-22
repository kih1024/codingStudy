N, M = map(int, input().split())
graph = [[1e9] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
result = 0
ans = []

for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        # i에서 j가 서로 이어져 있는지 확인 하는 것이다. 이어져만 있다면 i와 j중 어느쪽이 큰지 확인할수 있다
        # i<j라면 graph[i][j] 가 1e9가 나오면 안된다,i>j 라면 graph[j][i] 가 1e9가 나오면 안됨.
        if graph[i][j] != 1e9 or graph[j][i] != 1e9:
            count += 1

    if count == N:
        ans.append(i)
        result += 1

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         print(graph[i][j], end=" ")
#     print()

print(ans)
print(result)

