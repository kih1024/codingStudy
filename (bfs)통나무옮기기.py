# bfs 문제 dfs로 될수는 있는데 시간초과 날것이다.
# 최소 몇회라는 조건이 달렸음으로 낮은 depth부터 검색하는 bfs가 빠름

from collections import deque


def bfs(depth):
    dq = deque([[start, depth]])

    while dq:
        node, d = dq.popleft()
        # print(node, d)
        f, s, t = node
        if node == end:
            return d
        if (f, s, t) not in visited:
            visited[(f, s, t)] = True
            # print(node, d)
            for i in range(5):
                is_rotate = True
                if i == 4:
                    r, c = s // N, s % N
                    for j in range(8):
                        ny = r + is_y[j]
                        nx = c + is_x[j]
                        if ny >= N or ny < 0 or nx >= N or nx < 0:
                            is_rotate = False
                            break
                        if arr[ny][nx] == "1":
                            is_rotate = False
                            break
                    if is_rotate:
                        if s - f == 1:
                            f, t = s - N, s + N
                        else:
                            f, t = s - 1, s + 1
                        if (f, s, t) not in visited:
                            dq.append([[f, s, t], d + 1])
                else:
                    fy, fx = f // N, f % N
                    sy, sx = s // N, s % N
                    ty, tx = t // N, t % N
                    for j in range(4):
                        nfy, nfx = fy + dy[j], fx + dx[j]
                        nsy, nsx = sy + dy[j], sx + dx[j]
                        nty, ntx = ty + dy[j], tx + dx[j]
                        if nty >= N or nfy < 0 or ntx >= N or nfx < 0:
                            continue
                        if (
                            arr[nfy][nfx] == "1"
                            or arr[nsy][nsx] == "1"
                            or arr[nty][ntx] == "1"
                        ):
                            continue
                        nf = (nfy * N) + nfx
                        ns = (nsy * N) + nsx
                        nt = (nty * N) + ntx
                        if (nf, ns, nt) not in visited:
                            dq.append([[nf, ns, nt], d + 1])

    return 0


N = int(input())
arr = [list(input()) for i in range(N)]
answer = 1e9
start, end = [], []
is_y, is_x = [-1, 1, 1, -1, 0, 1, 0, -1], [1, 1, -1, -1, 1, 0, -1, 0]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = dict()

for i in range(N):
    for j in range(N):
        if arr[i][j] == "B":
            start.append((i * N) + j)
        if arr[i][j] == "E":
            end.append((i * N) + j)
# print(start,end)

print(bfs(0))
