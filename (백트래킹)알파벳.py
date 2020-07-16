# https://www.acmicpc.net/problem/1987
# r, c = map(int, input().split())
# m = [list(map(lambda x: ord(x) - 65, input())) for i in range(r)]
# print(m)

# 시간 초과 코드
# import sys

# input = sys.stdin.readline


# def dfs(row, col, count):
#     global result
#     result = max(count, result)
#     visit.append(alpha[row][col])
#     # print(visit)
#     for i in range(4):
#         dy = row + y[i]
#         dx = col + x[i]
#         if 0 <= dy < r and 0 <= dx < c:
#             if alpha[dy][dx] not in visit:
#                 dfs(dy, dx, count + 1)
#                 visit.remove(alpha[dy][dx])
#                 # print(visit)


# r, c = map(int, input().split())
# alpha = [list(input().strip()) for _ in range(r)]
# visit = []
# x = [1, 0, -1, 0]
# y = [0, 1, 0, -1]

# result = 0
# dfs(0, 0, 1)
# print(result)


import sys

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])
    print(q)
    while q:
        x, y, ans = q.pop()

        # 좌우상하 갈 수 있는지 살펴본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx, ny, ans + board[nx][ny]))
                print(q)
                answer = max(answer, len(ans) + 1)


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
BFS(0, 0)
print(answer)
