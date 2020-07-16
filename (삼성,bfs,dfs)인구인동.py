from collections import deque


def bfs(row, col):
    dq = deque([(row, col)])
    count, sumV = 0, 0
    unioned = False
    road = []
    while dq:
        now = dq.popleft()
        r, c = now[0], now[1]
        if visited[r][c] == False:
            visited[r][c] = True
            count += 1
            sumV += arr[r][c]
            road.append((r, c))
            for i in range(4):
                y = dy[i] + r
                x = dx[i] + c
                if y < 0 or y >= n or x < 0 or x >= n:
                    continue
                temp = abs(arr[y][x] - arr[r][c])
                if visited[y][x] == True or temp < ll or temp > rr:
                    continue
                unioned = True
                dq.append((y, x))

    if not unioned:
        visited[row][col] = False
        return False
    else:
        for r, c in road:
            new_v = sumV // count
            arr[r][c] = new_v
        return True


n, ll, rr = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 0

while True:
    isUnion = False
    visited = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                continue
            if bfs(i, j):
                isUnion = True

    if not isUnion:
        break

    answer += 1

print(answer)
