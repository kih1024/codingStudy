from collections import deque
import sys

input = sys.stdin.readline


def BFS(y, x, d):
    dq = deque([(y, x, d)])
    visited[y][x][d] = 1
    while dq:
        y, x, d = dq.popleft()
        
        if arr[y][x] == '1':
            return visited[y][x][d] - 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if arr[ny][nx] != "#" and visited[ny][nx][d] == 0:
                asc = ord(arr[ny][nx])
                if 65 <= asc <= 90:
                    if d & (1 << asc - ord('A')):
                        visited[ny][nx][d] = visited[y][x][d] + 1
                        dq.append((ny,nx,d))
                elif 97 <= asc <= 122:
                    nd = d | (1 << asc - ord('a'))
                    if visited[ny][nx][nd] == 0:
                        visited[ny][nx][nd] = visited[y][x][d] + 1
                        dq.append((ny,nx,nd))
                else:
                    visited[ny][nx][d] = visited[y][x][d] + 1
                    dq.append((ny,nx,d))
    return -1

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
N, M = map(int, input().split())
arr = []
pocket = []
pocket_idx = []
visited = [[[0]*64 for _ in range(M)] for _ in range(N)]
for i in range(N):
    t = list(input())
    arr.append(t)
    for j, k in enumerate(t):
        if k == "0":
            now_y, now_x = i, j

ans = BFS(now_y, now_x, 0)
print(ans)
