def process():
    # 세대 반복횟수
    for i in range(g):
        nowT = temp[-1]
        length = len(temp)
        # 현재 세대 좌표들을 마지막부터 처음점 순으로 돌린다.
        for k in range(length - 2, -1, -1):
            nowW = temp[-1]
            tempY = temp[k][0] - nowT[0]
            tempX = temp[k][1] - nowT[1]
            for j in range(4):
                if dy[j] == tempY and dx[j] == tempX:
                    idx = j
            addV = [nowW[0] + dy[(idx - 1) % 4], nowW[1] + dx[(idx - 1) % 4]]
            temp.append(addV)
            nowT = temp[k]

    for i in temp:
        b[i[0]][i[1]] = 1


n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
# 오른쪽 위 왼족 아래
# 0 1 2 3
dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]
b = [[0] * 101 for i in range(101)]
ans = 0
for i in range(n):
    x, y, d, g = arr[i]
    temp = [[y, x]]
    now = [y + dy[d], x + dx[d]]
    temp.append(now)
    process()

for i in range(100):
    for j in range(100):
        if b[i][j] and b[i + 1][j] and b[i][j + 1] and b[i + 1][j + 1]:
            ans += 1

print(ans)
