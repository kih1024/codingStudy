from copy import deepcopy


def spread(arr):
    global r, c
    new = deepcopy(arr)
    dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 0 or arr[i][j] == -1:
                continue
            temp = []
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if y < 0 or y >= r or x < 0 or x >= c:
                    continue
                if arr[y][x] != -1:
                    temp.append([y, x])
            countD = len(temp)
            mount = arr[i][j] // 5
            for rr, cc in temp:
                new[rr][cc] += mount
            new[i][j] -= mount * countD

    return new


def rotate(row, row2, arr):
    global r, c
    new = deepcopy(arr)
    # 오른쪽 위 왼쪽 아래
    dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]
    count = [c - 2, row, c - 1, row - 1]
    rr, cc = row, 1
    for i in range(4):
        for _ in range(count[i]):
            rrr, ccc = rr + dy[i], cc + dx[i]
            new[rrr][ccc] = arr[rr][cc]
            rr, cc = rrr, ccc
    new[row][1] = 0
    # 오른쪽 아래 왼쪽 위
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    count = [c - 2, r - 1 - row2, c - 1, (r - 1 - row2) - 1]
    rr, cc = row2, 1
    for i in range(4):
        for _ in range(count[i]):
            rrr, ccc = rr + dy[i], cc + dx[i]
            new[rrr][ccc] = arr[rr][cc]
            rr, cc = rrr, ccc
    new[row2][1] = 0

    return new


r, c, t = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    if m[i][0] == -1:
        f, s = i, i + 1
        break

for _ in range(t):
    m = spread(m)
    m = rotate(f, s, m)

answer = 2
for i in m:
    answer += sum(i)
print(answer)
