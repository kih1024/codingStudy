# https://www.acmicpc.net/problem/14502

from itertools import combinations
from copy import deepcopy
from collections import deque


def wall():
    global emptyC
    for i in list(combinations(empty, 3)):
        li = deepcopy(arr)
        for j in range(3):
            li[i[j] // m][i[j] % m] = 1
        temp = wallC + 3
        birusC = bfs(li, pos_two)
        emptyC = max(((m * n) - temp - birusC), emptyC)
    return emptyC


# pos : 2의 위치들
def bfs(li, pos):
    # visit = [[0] * m for i in range(n)]
    visit = [[False] * m for _ in range(n)]
    dq = deque(pos)
    count = 0
    while dq:
        r, c = dq.popleft()
        if visit[r][c] == False:
            visit[r][c] = True
            count += 1
            for i in range(4):
                dy = r + y[i]
                dx = c + x[i]
                if dy < 0 or dy > n - 1 or dx < 0 or dx > m - 1:
                    continue
                if li[dy][dx] == 0:
                    if visit[dy][dx] == False:
                        li[dy][dx] == 2
                        dq.append((dy, dx))

    return count


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
pos_two = []
empty = []
wallC = 0
emptyC = 0
x = [1, 0, -1, 0]
y = [0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty.append((i * m) + j)
        elif arr[i][j] == 2:
            pos_two.append((i, j))
        else:
            wallC += 1

print(wall())
