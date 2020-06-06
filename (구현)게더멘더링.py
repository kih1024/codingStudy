def ck(y, x, d1, d2):
    global N
    gather = [0, 0, 0, 0, 0]
    for r in range(N):
        for c in range(N):
            if r < y + d1 and c <= x and ((r < y) or (c < x - (r - y))):
                gather[0] += arr[r][c]
            elif r <= y + d2 and c <= N - 1 and ((r < y) or (c > x + (r - y))):
                gather[1] += arr[r][c]
            elif (
                y + d1 <= r
                and c < x - d1 + d2
                and (r > y + d1 + d2 or c < (x - d1 + d2 - (y + d1 + d2 - r)))
            ):
                gather[2] += arr[r][c]
            elif (
                y + d2 < r
                and x - d1 + d2 <= c
                and (r > y + d1 + d2 or c > (x - d1 + d2 + (y + d1 + d2 - r)))
            ):
                gather[3] += arr[r][c]
            else:
                gather[4] += arr[r][c]

    return max(gather) - min(gather)


N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
answer = 1e9
for i in range(N):
    for j in range(N):
        for d1 in range(1, N):
            if j - d1 < 0:
                break
            for d2 in range(1, N):
                if i + d1 + d2 > N - 1 or j + d2 > N - 1:
                    break

                answer = min(answer, ck(i, j, d1, d2))

print(answer)
