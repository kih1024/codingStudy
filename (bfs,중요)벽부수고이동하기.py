import sys
from collections import deque


def bfs():
    dq = deque([(0, 0, 1, 1)])

    while dq:
        # j: 남은 공사 횟수 d: depth 길이
        r, c, j, d = dq.popleft()

        if r == N - 1 and c == M - 1:
            return d

        for i in range(4):
            y = r + dy[i]
            x = c + dx[i]
            if y >= N or y < 0 or x >= M or x < 0:
                continue
            # 빈공간지나깔때
            if not visited[j][y][x] and arr[y][x] == 0:
                visited[0][y][x] = True
                if j:
                    visited[1][y][x] = True
                dq.append((y, x, j, d + 1))
            # 벽 일때
            elif j and arr[y][x]:
                visited[0][y][x] = True
                dq.append((y, x, 0, d + 1))
    return -1


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for i in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
visited = [[[False] * M for i in range(N)] for i in range(2)]
print(bfs())
