from collections import deque


def move(l):
    li = [i for i in l]
    for i in range(len(li)):
        if li[i] == "R" or li[i] == "B":
            for j in range(i - 1, -1, -1):
                if li[j] == "#" or li[j] == "R" or li[j] == "B":
                    li[j + 1], li[i] = li[i], li[j + 1]
                    break
                elif li[j] == "O":
                    if li[i] == "B":
                        marble[1] = True
                    if li[i] == "R":
                        marble[0] = True
                    li[i] = "."
                    break
    return li


def rotate(m, rl, cl):
    nm = [[0] * rl for _ in range(cl)]
    for i in range(rl):
        for j in range(cl):
            nm[j][rl - i - 1] = m[i][j]
    return nm


# 이 부분만 다시 보자
def bfs(arr, d):
    dq = deque([[arr, d]])
    while dq:
        now = dq.popleft()
        board, depth = now[0], now[1]
        for z in range(4):
            new_board = [move(i) for i in board]
            r_board = rotate(board, len(board), len(board[0]))
            if new_board == board:
                board = r_board
                continue
            if marble[1] == True:
                board = r_board
                marble[0], marble[1] = False, False
                continue
            if marble[0] == True:
                return depth + 1
            if depth + 1 <= 9:
                dq.append([new_board, depth + 1])
            board = r_board
    return -1


n, m = map(int, input().split())
b = [list(input()) for i in range(n)]
marble = [False, False]
answer = bfs(b, 0)
print(answer)
