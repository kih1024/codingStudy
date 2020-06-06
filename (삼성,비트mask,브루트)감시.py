# https://www.acmicpc.net/problem/15683


def fill(y, x, i, f):
    # i 는 direc의 값들
    for k in range(4):
        if i & (1 << k):
            ny, nx = y, x
            while True:
                if ny < 0 or ny >= n or nx < 0 or nx >= m or arr[ny][nx] == 6:
                    break
                b[ny][nx] += f
                ny, nx = ny + dy[k], nx + dx[k]


def dfs(idx):
    global answer
    if idx == len(camera):
        area = 0
        for i in range(n):
            area += b[i].count(0)
        answer = min(answer, area)
        return

    y, x, value = camera[idx]
    temp = direc[value]
    for i in temp:
        fill(y, x, i, 1)
        dfs(idx + 1)
        fill(y, x, i, -1)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
b = [[0] * m for i in range(n)]
camera = []
answer = 1e9
U, R, D, L = 1, 2, 4, 8
direc = [
    [],
    [U, R, D, L],
    [R | L, U | D],
    [U | R, R | D, D | L, L | U],
    [R | D | L, U | D | L, U | R | L, U | R | D],
    [U | R | D | L],
]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 6:
            b[i][j] = 1
        elif arr[i][j] != 0:
            camera.append((i, j, arr[i][j]))
dfs(0)
print(answer)


# from sys import stdin

# input = stdin.readline

# n, m = map(int, input().split())
# a = [[6] * (m + 2)]
# b = [[0] * (m + 2) for _ in range(n + 2)]
# v = []
# ans = 1e9
# dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
# U, R, D, L = 1, 2, 4, 8
# direct = [
#     [0],
#     [U, R, D, L],
#     [U | D, R | L],
#     [U | R, R | D, D | L, L | U],
#     [L | U | R, U | R | D, R | D | L, D | L | U],
#     [U | R | D | L],
# ]


# def init():
#     for _ in range(n):
#         a.append([6] + list(map(int, input().split())) + [6])
#     a.append(list([6] * (m + 2)))
#     for i in range(n + 2):
#         for j in range(m + 2):
#             if a[i][j] == 6:
#                 b[i][j] = 1
#             elif a[i][j]:
#                 v.append((i, j, a[i][j]))


# def observe(x, y, i, d):
#     for k in range(4):
#         if i & (1 << k):
#             nx, ny = x, y
#             while a[nx][ny] != 6:
#                 b[nx][ny] += d
#                 nx, ny = nx + dx[k], ny + dy[k]


# def solve(index):
#     global ans
#     if index == len(v):
#         area = 0
#         for i in range(1, n + 1):
#             area += b[i].count(0)
#         ans = min(ans, area)
#         return
#     x, y, ids = v[index]
#     for i in direct[ids]:
#         observe(x, y, i, 1)
#         solve(index + 1)
#         observe(x, y, i, -1)


# init()
# solve(0)
# print(ans)
