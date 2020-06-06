# https://www.acmicpc.net/problem/17135

import sys
from copy import deepcopy

def select(arr, archer):
    global d
    result = []
    for a in archer:
        temp = []
        isValid = False
        for i in range(m):
            for j in range(n):
                distance = abs(a[0] - i) + abs(a[1] - j)
                if arr[i][j] == 1 and distance <= d:
                    isValid = True
                    temp.append([distance, i, j])
        if isValid:
            temp.sort()
            result.append((temp[0][1], temp[0][2]))

    return result

def defence(count):
    global idx, kill
    if count == 0:
        return kill
    archer = [[idx[0], -1], [idx[1], -1], [idx[2], -1]]
    target = set(select(new_arr, archer))
    for t in target:
        new_arr[t[0]][t[1]] = 0
        kill += 1
    for i in range(m):
        new_arr[i][: n - 1] = new_arr[i][1:n]
        new_arr[i][n - 1] = 0
    return defence(count - 1)

input = sys.stdin.readline
n, m, d = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
new = [[0] * n for i in range(m)]
answer = 0
isFirst = False
fr = 0
# 90도 회전
for i in range(n):
    for j in range(m):
        if not isFirst and arr[i][j] == 1:
            isFirst = True
            fr = n - i
        new[j][n - 1 - i] = arr[i][j]

for idx in [[i,j,k] for i in range(m-2) for j in range(i+1, m-1) for k in range(j+1,m)]:
    new_arr = deepcopy(new)
    kill = 0
    answer = max(answer, defence(fr))

print(answer)


# from copy import deepcopy

# N, M, D = map(int, input().split())
# B = [list(map(int, input().split())) for _ in range(N)]

# def hunt(h, C):
#     for d in range(1, D + 1):
#         for dx in range(-d, d + 1):
#             x, y = h + dx, N - (d - abs(dx))
#             if 0 <= x < M and 0 <= y < N and C[y][x]: return x, y

# def sol(H):
#     C = deepcopy(B)
#     ret = 0
#     for _ in range(N):
#         E = set(hunt(h, C) for h in H) - {None}
#         ret += len(E)
#         for x, y in E: C[y][x] = 0
#         for y in range(N - 1, 0, -1): C[y] = C[y - 1][:]
#         C[0] = [0] * M
#     return ret

# print(max(sol([i, j, k]) for i in range(M - 2) for j in range(i + 1, M - 1) for k in range(j + 1, M)))