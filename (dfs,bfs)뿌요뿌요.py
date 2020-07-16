# https://www.acmicpc.net/problem/16768
from collections import deque


def bfs(r, c):
    count = 0
    dq = deque([(r, c)])
    while dq:
        now = dq.popleft()
        row = now[0]
        col = now[1]
        if visit[row][col] == False:
            visit[row][col] = True
            count += 1
            dup.append((row, col))
            for j in range(4):
                dy = row + y[j]
                dx = col + x[j]
                if dy < 0 or dy > n - 1 or dx < 0 or dx > 9:
                    continue
                if visit[dy][dx] == False and arr[row][col] == arr[dy][dx]:
                    dq.append((dy, dx))
    if count >= k:
        return True
    else:
        return False


def zero():
    for row, col in dup:
        arr[row][col] = "0"


def down():
    for j in range(10):
        temp = []
        for i in range(n - 1, -1, -1):
            if arr[i][j] != "0":
                temp.append(arr[i][j])

        for i in range(n - 1, -1, -1):
            if (n - 1) - i >= len(temp):
                arr[i][j] = "0"
            else:
                arr[i][j] = temp[(n - 1) - i]


n, k = map(int, input().split())
arr = [list(input()) for i in range(n)]
y = [0, 1, 0, -1]
x = [1, 0, -1, 0]
check = True
while check:
    check = False
    visit = [[False] * 10 for i in range(n)]
    down()
    for i in range(n):
        for j in range(10):
            if arr[i][j] == "0":
                continue
            dup = []
            if bfs(i, j):
                check = True
                zero()

for i in range(n):
    print("".join(arr[i]))