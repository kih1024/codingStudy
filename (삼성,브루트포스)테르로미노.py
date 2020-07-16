def process(r, c):
    global maxV
    for i in range(19):
        ck = True
        temp = []
        for j in range(4):
            y = r + dy[i][j]
            x = c + dx[i][j]
            if y < 0 or y >= n or x < 0 or x >= m:
                ck = False
                break
            temp.append(arr[y][x])
        if ck:
            maxV = max(maxV, sum(temp))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
maxV = 0
dx = [
    [0, 0, 1, 2],
    [1, 1, 1, 0],
    [0, 1, 2, 2],
    [0, 1, 0, 0],
    [2, 2, 1, 0],
    [0, 1, 1, 1],
    [0, 1, 2, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 2],
    [0, 0, 0, 1],
    [0, 1, 2, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 2],
    [1, 1, 0, 0],
    [0, 1, 1, 2],
    [0, 1, 2, 3],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
]
dy = [
    [0, 1, 1, 1],
    [0, 1, 2, 2],
    [0, 0, 0, 1],
    [0, 0, 1, 2],
    [0, 1, 1, 1],
    [0, 0, 1, 2],
    [0, 0, 0, 1],
    [0, 1, 2, 2],
    [0, 1, 1, 1],
    [0, 1, 2, 1],
    [0, 0, 0, 1],
    [1, 0, 1, 2],
    [0, 1, 1, 2],
    [1, 1, 0, 0],
    [0, 1, 1, 2],
    [0, 0, 1, 1],
    [0, 0, 0, 0],
    [0, 1, 2, 3],
    [0, 0, 1, 1],
]


for i in range(n):
    for j in range(m):
        process(i, j)

print(maxV)


# def dfs(idx, depth, a):
#     visit[idx] = 1
#     temp = deepcopy(a)
#     temp.append(idx)
#     if depth == 3:
#         if sum(temp) not in sum_idx:
#             sum_idx.append(sum(temp))
#             li.add(tuple(temp))
#             visit[idx] = 0
#         return

#     row = idx // m
#     col = idx % m

#     for i in range(4):
#         if row + y[i] < 0 or row + y[i] >= n or col + x[i] < 0 or col + x[i] >= m:
#             continue
#         t = (row + y[i]) * m + (col + x[i])
#         if visit[t] == 0:
#             dfs(t, depth + 1, temp)

#     visit[idx] = 0


# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for i in range(n)]
# maxV = 0
# y, x = [0, 1, 0, -1], [1, 0, -1, 0]
# visit = [0] * (n * m)
# li = set()
# sum_idx = []
# for i in range(n * m):
#     dfs(i, 0, [])

# print(li)
# for i in li:
#     sumV = 0
#     for j in i:
#         row = j // m
#         col = j % m
#         sumV += arr[row][col]
#     maxV = max(maxV, sumV)

# print(maxV)
