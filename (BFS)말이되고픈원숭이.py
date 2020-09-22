from collections import deque
import sys

input = sys.stdin.readline

def BFS():
    global K, W, H
    dq = deque([(0, K, 0)])
    visited[K][0][0] = True

    while dq:
        now, kk, cnt = dq.popleft()
        y, x = now // W, now % W
        horse = False
        if y == H - 1 and x == W - 1:
            return cnt

        for i in range(12):
            if kk == 0 and i == 4:
                break
            ny, nx = y + dy[i], x + dx[i]
            if i >= 4:
                horse = True
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            nk = kk
            if horse:
                nk = kk - 1
            if arr[ny][nx] == 0 and not visited[nk][ny][nx]:
                visited[nk][ny][nx] = True
                dq.append(((ny * W) + nx, nk, cnt + 1))
    return -1

dy, dx = (
    [0, 1, 0, -1, -2, -1, 1, 2, 2, 1, -1, -2],
    [1, 0, -1, 0, 1, 2, 2, 1, -1, -2, -2, -1],
)
K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
visited = [[[False] * W for _ in range(H)] for _ in range(K + 1)]

ans = BFS()
print(ans)
