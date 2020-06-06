import sys

sys.setrecursionlimit(100000)


def combination(n, cnt, s):
    if arr[n // 5][n % 5] == "S":
        s += 1

    visited[n] = True
    mapp[n // 5][n % 5] = True

    if cnt == 7:
        if s >= 4:
            find()
    else:
        for i in range(n + 1, 25):
            if not visited[i]:
                combination(i, cnt + 1, s)

#  빽트래킹
    visited[n] = False
    mapp[n // 5][n % 5] = False


def find():
    global cnt
    for i in range(25):
        if visited[i]:
            y, x = i // 5, i % 5

            visit = [[False] * 5 for i in range(5)]
            visit[y][x] = True
            cnt = 1
            isConnect(y, x, visit)
            return


def isConnect(y, x, ck):
    global cnt,ans
    if cnt == 7:
        ans += 1
    else:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= 5 or ny < 0 or nx >= 5 or nx < 0:
                continue
            if mapp[ny][nx] and not ck[ny][nx]:
                ck[ny][nx] = True
                cnt += 1
                isConnect(ny, nx, ck)


arr = [list(input()) for _ in range(5)]
cnt = 0
ans = 0
visited = [False] * 25
mapp = [[False] * 5 for i in range(5)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(25):
    combination(i, 1, 0)

print(ans)
# for i in comb:

