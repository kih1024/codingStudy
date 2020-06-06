def dfs(r, c, b, d, count):
    global answer
    print(r,c)
    if r == len(b) - 1 and c == len(b) - 1:
        # count += 100
        answer = min(answer, count)
        return

    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]
        if nr < 0 or nr >= len(b) or nc < 0 or nc >= len(b):
            continue
        if b[nr][nc] == 1:
            continue

        if i != d:
            count += 500
            count += 100
            b[nr][nc] = 1
            dfs(nr, nc, b, i, count)
            count -= 500
            count -= 100
            b[nr][nc] = 0
        else:
            count += 100
            b[nr][nc] = 1
            dfs(nr, nc, b, i, count)
            count -= 100
            b[nr][nc] = 0


dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 1e9

def solution(board):
    global answer
    # 오른쪽 아래 왼쪽 위
    for i in range(4):
        dfs(0, 0, board, i, 0)
    return answer

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))