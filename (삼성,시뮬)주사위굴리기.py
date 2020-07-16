def move(li):
    temp = li[-1]
    li[1:] = li[0:3]
    li[0] = temp


def rotate(d):
    # 오른쪽으로 돌릴때
    if d == 0:
        li = [dice[0], dice[2], dice[5], dice[3]]
        move(li)
        dice[0], dice[2], dice[5], dice[3] = [i for i in li]
    # 왼쪽으로 돌릴때
    elif d == 1:
        li = [dice[0], dice[3], dice[5], dice[2]]
        move(li)
        dice[0], dice[3], dice[5], dice[2] = [i for i in li]
    # 위로 돌릴때
    elif d == 2:
        li = [dice[0], dice[1], dice[5], dice[4]]
        move(li)
        dice[0], dice[1], dice[5], dice[4] = [i for i in li]
    # 아래로 돌릴때
    else:
        li = [dice[0], dice[4], dice[5], dice[1]]
        move(li)
        dice[0], dice[4], dice[5], dice[1] = [i for i in li]

    if arr[y][x] == 0:
        arr[y][x] = dice[-1]
    else:
        dice[-1] = arr[y][x]
        arr[y][x] = 0


n, m, y, x, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
order = [i - 1 for i in list(map(int, input().split()))]

dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
# 위 앞 오른쪽 왼쪽 뒤 아래
dice = [0] * 6
for i in order:
    # d : 0 동,1 서,2 북,3 남
    if y + dy[i] > n - 1 or y + dy[i] < 0 or x + dx[i] > m - 1 or x + dx[i] < 0:
        continue
    y = y + dy[i]
    x = x + dx[i]
    rotate(i)
    print(dice[0])
