from collections import deque


def bfs(r, c):
    global save
    dq = deque([(r, c)])
    temp = []
    while dq:
        y, x = dq.popleft()

        if not visited[y][x]:
            visited[y][x] = True
            temp.append((y, x))
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny >= 12 or ny < 0 or nx >= 6 or nx < 0:
                    continue
                if not visited[ny][nx] and arr[ny][nx] == arr[r][c]:
                    dq.append((ny, nx))

    if len(temp) >= 4:
        save = temp
        return True
    else:
        return False


def kill():
    for r, c in save:
        arr[r][c] = "."


def down():
    for j in range(6):
        temp = []
        for i in range(11, -1, -1):
            if arr[i][j] != ".":
                temp.append(arr[i][j])

        for i in range(11, -1, -1):
            if 11 - i >= len(temp):
                arr[i][j] = "."
            else:
                arr[i][j] = temp[11 - i]


arr = [list(input()) for _ in range(12)]
count = 0
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
while True:
    down()
    is_puyo = False
    visited = [[False] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            save = []
            if arr[i][j] == ".":
                continue
            if bfs(i, j):
                # print(save)
                kill()
                is_puyo = True

    if is_puyo:
        count += 1
    else:
        break

print(count)
