# https://www.acmicpc.net/problem/3085

import sys

input = sys.stdin.readline

def ck():
    global answer
    temp = 1
    # 행 탐색
    for i in range(N):
        count = 1
        for j in range(1, N):
            if arr[i][j] == arr[i][j - 1]:
                count += 1
            else:
                answer = max(answer, count)
                if answer == N:
                    return
                count = 1
        answer = max(answer, count)
        if answer == N:
            return

    # 열 탐색
    for i in range(N):
        count = 1
        for j in range(1, N):
            if arr[j][i] == arr[j - 1][i]:
                count += 1
            else:
                answer = max(answer, count)
                if answer == N:
                    return
                count = 1
        answer = max(answer, count)
        if answer == N:
            return


N = int(input())

arr = [list(input()) for i in range(N)]
dy, dx = [0, 1], [1, 0]
answer = 0
ck()

for i in range(N):
    for j in range(N):
        for k in range(2):
            y = i + dy[k]
            x = j + dx[k]
            if y >= N or y < 0 or x >= N or x < 0:
                continue
            arr[i][j], arr[y][x] = arr[y][x], arr[i][j]
            ck()
            arr[i][j], arr[y][x] = arr[y][x], arr[i][j]
            if answer == N:
                print(N)
                exit(0)

print(answer)

