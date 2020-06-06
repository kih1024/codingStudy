import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(y, x):
    if y == M - 1 and x == N - 1:
        return 1
    if dp[y][x] != -1: #방문 했던 길 이라면:
        return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny >= M or ny < 0 or nx >= N or nx < 0:
            continue
        if arr[ny][nx] < arr[y][x]:
            dp[y][x] += dfs(ny, nx)
    return dp[y][x]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
print(dfs(0, 0))

