import sys

N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
tree = [[] for _ in range(N * N)]
for i in range(M):
    y, x, z = map(int, sys.stdin.readline().split())
    tree[(y-1) * N + (x-1)].append(z)
arr = [[5] * N for _ in range(N)]
dy, dx = (0, 1, 1, 1, 0, -1, -1, -1), (1, 1, 0, -1, -1, -1, 0, 1)

for year in range(K):
    # 봄
    die = []
    for i in range(len(tree)):
        if len(tree[i]) >= 1:
            r, c = i // N, i % N
            num = len(tree[i])
            tree[i] = sorted(tree[i])
            temp = []
            for j in range(len(tree[i])):
                if tree[i][j] <= arr[r][c]:
                    arr[r][c] = arr[r][c] - tree[i][j]
                    temp.append(tree[i][j] + 1)
                else:
                    die.append((r, c, tree[i][j]))
            tree[i] = temp
    # 여름
    for r, c, nu in die:
        arr[r][c] += nu // 2
    # 가을
    pos = []
    for i in range(len(tree)):
        r, c = i // N, i % N
        for j in range(len(tree[i])):
            if tree[i][j] % 5 == 0:
                for d in range(8):
                    yy = r + dy[d]
                    xx = c + dx[d]
                    if yy < 0 or yy >= N or xx < 0 or xx >= N:
                        continue
                    tree[(yy * N) + xx].append(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            arr[i][j] += A[i][j]

answer = 0
for t in tree:
    answer += len(t)

print(answer)
