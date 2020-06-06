from collections import deque


def bfs(r, c):
    dq = deque([(r, c)])
    seaP = []
    while dq:
        rr, cc = dq.popleft()
        if not visited[rr][cc]:
            visited[rr][cc] = 1
            for i in range(4):
                y = rr + dy[i]
                x = cc + dx[i]
                if y < 0 or y >= N or x < 0 or x >= M:
                    continue
                if arr[y][x] == 0:
                    seaP.append((rr, cc))

                if not visited[y][x] and arr[y][x] == 1:
                    dq.append((y, x))
    return set(seaP)


def ck(k, z, minV):
    rc = [M, N]
    for x in [0, 1]:
        for t in [1, -1]:
            if k[x] == z[x]:
                temp = k[x ^ 1]
                for _ in range(abs(k[x ^ 1] - z[x ^ 1])):
                    temp += t
                    if temp >= rc[x] or temp < 0:
                        break
                    if x == 0:
                        if arr[k[x]][temp] == 1:
                            break
                    else:
                        if arr[temp][k[x]] == 1:
                            break
                if temp == z[x ^ 1]:
                    r = abs(k[x ^ 1] - z[x ^ 1]) - 1
                    if r >= 2:
                        minV = min(minV, r)
                else:
                    continue
    return minV


def distance(a):
    graph = []
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            minV = 1e9
            for k in a[i]:
                for z in a[j]:
                    minV = ck(k, z, minV)

            if minV != 1e9:
                graph.append((minV, i, j))
                graph.append((minV, j, i))
    return graph


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if root1 != root2:
        parent[root2] = root1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
visited = [[0] * M for i in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
parent = dict()
idx = 0
seaA, li = [], []
answer = 0
# 0방문 1방문 x

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            visited[i][j] = 1
            continue
        if not visited[i][j]:
            seaA.append(bfs(i, j))
            parent[idx] = idx
            idx += 1

edges = sorted(distance(seaA))

for edge in edges:
    w, v, u = edge
    if find(v) != find(u):
        union(v, u)
        li.append(edge)

if len(li) == len(parent) - 1:
    for i in li:
        answer += i[0]
    print(answer)
else:
    print(-1)
