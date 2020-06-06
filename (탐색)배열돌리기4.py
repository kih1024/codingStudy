# https://www.acmicpc.net/problem/17406
from copy import deepcopy

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
query = [list(map(int, input().split())) for i in range(k)]
answer = 1000000
dy, dx = [1, 0, -1, 0], [0, -1, 0, 1]


def sumV(arr):
    return min(sum(i) for i in arr)


def move(arr, q):
    new_arr = deepcopy(arr)
    row, col = q[0] - 1, q[1] - 1
    s = q[2]
    for i in range(1, s + 1):
        r, c = row - i, col + i
        for j in range(4):
            for z in range(i * 2):
                rr, cc = r + dy[j], c + dx[j]
                new_arr[rr][cc] = arr[r][c]
                r, c = rr, cc
    return new_arr


def dfs(arr, q):
    global answer
    if sum(q) == k:
        answer = min(answer, sumV(arr))
        return answer
    for i in range(k):
        if q[i] == 0:
            new_arr = move(arr, query[i])
            q[i] = 1
            dfs(new_arr, q)
            q[i] = 0


qry = [0 for _ in range(k)]
dfs(arr, qry)
print(answer)

