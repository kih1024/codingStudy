def ck(v, r, c):
    if v in arr[r]:
        return False

    for i in range(9):
        if arr[i][c] == v:
            return False

    rr, cc = r // 3, c // 3

    for i in range(rr * 3, (rr * 3) + 3):
        for j in range(cc * 3, (cc * 3) + 3):
            if arr[i][j] == v:
                return False

    return True


def dfs(idx):
    global isFind
    if idx == len(zero_pos):
        isFind = True
        return

    r, c = zero_pos[idx]

    for v in range(1, 10):
        if not ck(v, r, c):
            continue
        visited[r][c] = True
        arr[r][c] = v
        dfs(idx + 1)
        if isFind:
            return
        arr[r][c] = 0
        visited[r][c] = False


arr = [list(map(int, input().split())) for _ in range(9)]
zero_pos = []
answer = 0
isFind = False
visited = [[False] * 9 for i in range(9)]
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero_pos.append((i, j))

dfs(0)
for i in range(9):
    for j in range(9):
        arr[i][j] = str(arr[i][j])
    li = " ".join(arr[i])
    print(li)
