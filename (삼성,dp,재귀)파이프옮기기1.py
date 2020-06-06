# 이 방법은 백트래킹, 하지만 시간초과 했다. 파이썬은 dp로 풀어야 한다.


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

table = [[[0] * 3 for _ in range(n)] for _ in range(n)]
table[0][1][0] = 1

# 첫 위치에서 가로로만 이동하는 방법의 수
for x in range(2, n):
    if arr[0][x] == 0:
        table[0][x][0] = table[0][x - 1][0]

for y in range(1, n):
    for x in range(2, n):
        # 대각선으로 이동하는 경우
        if arr[y][x] == arr[y][x - 1] == arr[y - 1][x] == 0:
            table[y][x][2] = (
                table[y - 1][x - 1][0] + table[y - 1][x - 1][1] + table[y - 1][x - 1][2]
            )
        if arr[y][x] == 0:
            # 가로로 이동하는 경우
            table[y][x][0] = table[y][x - 1][2] + table[y][x - 1][0]
            # 세로로 이동하는 경우
            table[y][x][1] = table[y - 1][x][2] + table[y - 1][x][1]


print(sum(table[-1][-1]))

# def solve(y, x, z):
#     answer = 0

#     for i in range()
#     if y == n - 1 and x == n - 1:
#         return 1

#     for i in range(3):
#         if i + z == 1:
#             continue
#         ny = y + dy[i]
#         nx = x + dx[i]

#         if ny >= n or nx >= n or arr[ny][nx] == 1:
#             continue
#         if i == 2:
#             if arr[y][x + 1] == 1 or arr[y + 1][x] == 1:
#                 continue
#         answer += solve(ny, nx, i)
#     return answer


# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# # 가로 대각선 세로
# dy, dx = [0, 1, 1], [1, 0, 1]
# print(solve(0, 1, 0))
# # 끝점만 확인 하면된다.
