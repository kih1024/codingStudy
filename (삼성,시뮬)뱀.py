def move(hr, hc):
    if now_direc == 0:
        hc = hc + 1
    elif now_direc == 1:
        hr = hr + 1
    elif now_direc == 2:
        hc = hc - 1
    else:
        hr = hr - 1
    if hr < 0 or hr >= n or hc < 0 or hc >= n:
        return -1
    if [hr, hc] in snake[1:]:
        return -1
    if arr[hr][hc] == 2:
        arr[hr][hc] = 0
        snake.append([0, 0])
    snake[1:] = snake[0 : len(snake) - 1]
    snake[0] = [hr, hc]
    return 0


n, k = int(input()), int(input())
apple = [list(map(int, input().split())) for i in range(k)]
l = int(input())
# 동: 0 남 : 1 서 : 2 북: 3
now_direc = 0
count = 0
snake = [[0, 0]]
direc = [list(input().split()) for i in range(l)]
arr = [[0] * (n) for i in range(n)]

for ar, ac in apple:
    arr[ar - 1][ac - 1] = 2

while True:
    count += 1
    for i in direc:
        if int(i[0]) + 1 == count:
            if i[1] == "D":
                now_direc = (now_direc + 1) % 4
            else:
                now_direc = (now_direc - 1) % 4
    hr, hc = snake[0][0], snake[0][1]
    state = move(hr, hc)
    if state == -1:
        break

print(count)
