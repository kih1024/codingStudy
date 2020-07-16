import sys

input = sys.stdin.readline

def white(y, x, d, k):
    ny, nx = y + dy[d], x + dx[d]
    isFind = False
    temp = []
    for i, v in enumerate(E[y][x]):
        if v[0] == k + 1:
            isFind = True
            ii = i
        if not isFind:
            continue
        temp.append(E[y][x][i])
        C[v[0] - 1][0], C[v[0] - 1][1] = ny, nx
    E[ny][nx].extend(temp)
    del E[y][x][ii:]

def red(y, x, d, k):
    ny, nx = y + dy[d], x + dx[d]
    isFind = False
    temp = []
    for i, v in enumerate(E[y][x]):
        if v[0] == k + 1:
            isFind = True
            ii = i
        if not isFind:
            continue
        temp.append(E[y][x][i])
        C[v[0] - 1][0], C[v[0] - 1][1] = ny, nx
    reverse = temp[::-1]
    E[ny][nx].extend(reverse)
    del E[y][x][ii:]

def move(k):
    y, x, d = C[k][0], C[k][1], C[k][2]
    ny, nx = y + dy[d], x + dx[d]
    if B[ny][nx] == 0:
        white(y, x, d, k)
    elif B[ny][nx] == 1:
        red(y, x, d, k)
    else:
        if d % 2 != 0:
            d = d + 1
        else:
            d = d - 1
        C[k][2] = d
        for i, v in enumerate(E[y][x]):
            if v[0] == k + 1:
                E[y][x][i][1] = d
                break
        ny, nx = y + dy[d], x + dx[d]
        if B[ny][nx] == 0:
            white(y, x, d, k)
        elif B[ny][nx] == 1:
            red(y, x, d, k)
    return (ny, nx)

dy, dx = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
N, K = map(int, input().split())
B = [[2] * (N + 2)]
for i in range(N):
    B.append([2] + list(map(int, input().split())) + [2])
B.append([2] * (N + 2))
C = [list(map(int, input().split())) for _ in range(K)]
E = [[[] for _ in range(N + 2)] for _ in range(N + 2)]
for i in range(K):
    y, x, d = C[i][0], C[i][1], C[i][2]
    E[y][x].append([i + 1, d])

for t in range(1, 1001):
    for i in range(K):
        pos = move(i)
        if len(E[pos[0]][pos[1]]) >= 4:
            print(t)
            sys.exit()

print(-1)