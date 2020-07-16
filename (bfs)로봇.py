from collections import deque


def bfs(r, c, direc, depth):
    dq = deque([(r, c, direc, depth)])

    while dq:
        y, x, d, dp = dq.popleft()

        if [y, x, d] == end:
            return dp
        if (y, x, d) not in visited:
            visited[(y, x, d)] = True
            # print(y, x, d, dp)
            for i in range(3):
                if i == 0:
                    for j in range(1, 4):
                        ny = y + dy[d] * j
                        nx = x + dx[d] * j
                        if ny < N and ny >= 0 and nx < M and nx >= 0:
                            if arr[ny][nx] == 1:
                                break
                            if arr[ny][nx] == 0 and (ny, nx, d) not in visited:
                                # print("넣음1 : ", ny, nx, d, dp + 1)
                                dq.append((ny, nx, d, dp + 1))
                else:
                    if i == 1:
                        if (y, x, (d + 1) % 4) not in visited:
                            # print("넣음2 : ", y, x, (d + 1) % 4, dp + 1)
                            dq.append((y, x, (d + 1) % 4, dp + 1))
                    else:
                        if (y, x, (d - 1) % 4) not in visited:
                            # print("넣음3 : ", y, x, (d - 1) % 4, dp + 1)
                            dq.append((y, x, (d - 1) % 4, dp + 1))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
start = list(map(int, input().split()))
end = list(map(int, input().split()))
# visited = [[False] * M for i in range(N)]
visited = dict()
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
start[2] -= 1
end[2] -= 1

if start[2] == 1:
    start[2] = 2
elif start[2] == 2:
    start[2] = 1

if end[2] == 1:
    end[2] = 2
elif end[2] == 2:
    end[2] = 1
start[0], start[1] = start[0] - 1, start[1] - 1
end[0], end[1] = end[0] - 1, end[1] - 1

# print("시작:", start)
# print("끝:", end)

print(bfs(start[0], start[1], start[2], 0))
