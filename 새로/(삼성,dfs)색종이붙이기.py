def isCoverable(y, x, size, one2zero):
    for i in range(y, y + size):
        for j in range(x, x + size):
            if i >= 10 or j >= 10:
                return False
            else:
                if m[i][j] == 0:
                    return False
            one2zero.append([i, j])
    return True


def dfs(depth):
    global answer, totalOne
    # answer 보다 더 큰 depth는 탐색 할 필요 없음
    if depth >= answer and answer > 0:
        return
    if totalOne == 0:
        if answer == -1 or depth < answer:
            answer = depth
        return

    for y in range(10):
        for x in range(10):
            if m[y][x]:
                break
        if m[y][x]:
            break

    if m[y][x]:
        for size in range(1, 5 + 1):
            if paper[size]:
                one2zero = []
                if isCoverable(y, x, size, one2zero):
                    for r, c in one2zero:
                        m[r][c] = 0
                        
                    paper[size] -= 1
                    totalOne -= size ** 2
                    dfs(depth + 1)
                    paper[size] += 1
                    totalOne += size ** 2

                    for r, c in one2zero:
                        m[r][c] = 1


m = [list(map(int, input().split())) for i in range(10)]
totalOne = sum([sum(i) for i in m])
paper = [0] + [5] * 5
answer = -1
dfs(0)
print(answer)
