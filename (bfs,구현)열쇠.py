import sys
from collections import deque


def entrance():
    global N, M
    for k in [0, N - 1]:
        for j in range(M):
            if arr[k][j] == "." or arr[k][j] == "$":
                ent.append((k, j))
            elif ord(arr[k][j]) >= 97:
                ent.append((k, j))
                keys.append(chr(ord(arr[k][j]) - 32))
                arr[k][j] = "."
            elif arr[k][j] != "*":
                candidates.append((k, j, arr[k][j]))

    for k in [0, M - 1]:
        for i in range(1, N - 1):
            if arr[i][k] == "." or arr[i][k] == "$":
                ent.append((i, k))
            elif ord(arr[i][k]) >= 97:
                ent.append((i, k))
                keys.append(chr(ord(arr[i][k]) - 32))
                arr[i][k] = "."
            elif arr[i][k] != "*":
                candidates.append((i, k, arr[i][k]))


def bfs(e):
    global N, M, count
    dq = deque([e])
    new_key = []
    while dq:
        r, c = dq.popleft()
        if visited[r][c]:
            continue
        visited[r][c] = True
        if arr[r][c] == "$":
            count += 1
        for i in range(4):
            y, x = r + dy[i], c + dx[i]
            if y >= N or y < 0 or x >= M or x < 0:
                continue
            if not visited[y][x] and arr[y][x] != "*":
                if arr[y][x] == "." or arr[y][x] == "$":
                    dq.append((y, x))
                # 알파벳
                else:
                    # 대문자
                    if ord(arr[y][x]) < 97:
                        if arr[y][x] in keys:
                            arr[y][x] = "."
                            dq.append((y, x))
                    # 소문자
                    else:
                        dq.append((y, x))
                        new_key.append(chr(ord(arr[y][x]) - 32))
                        arr[y][x] = "."
    return new_key


dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
testcase = int(input())
for _ in range(testcase):
    answer = 0
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    keys = list(input())
    for i in range(len(keys)):
        if keys[i] == "0":
            keys = []
            break
        keys[i] = chr(ord(keys[i]) - 32)

    ent, candidates = [], []
    entrance()
    keys = set(keys)

    while True:
        visited = [[False] * M for i in range(N)]
        before = len(keys)
        temp = keys
        isValid = False
        count = 0
        for k in keys:
            for c in candidates:
                if c[2] == k:
                    ent.append((c[0], c[1]))
        # print(ent)
        for e in set(ent):
            new_key = bfs(e)
            temp = temp | set(new_key)
            if before != len(temp):
                isValid = True
        answer = count
        keys = temp
        if not isValid:
            break

    print(answer)
