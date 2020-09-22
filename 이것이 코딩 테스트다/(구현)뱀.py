def mapp():
    global N,ns
    print("-------------------------")
    print(ns)
    for i in range(N):
        print(arr[i])


N = int(input())
arr = [[-1] * N for _ in range(N)]
K = int(input())
apple = []
for _ in range(K):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 4
L = int(input())
snake = []
for _ in range(L):
    X, D = input().split()
    snake.append([int(X), D])

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
hr, hc, tr, tc = 0, 0, 0, 0
nd, ns = 0, 0
snake_i = 0
# 오른쪽 아래 왼쪽 위 : 0 1 2 3
arr[hr][hc] = 0
# print(arr)
while True:
    mapp()
    if ns == snake[snake_i][0]:
        if snake[snake_i][1] == "D":
            nd = (nd + 1) % 4
        else:
            nd = (nd - 1) % 4
        if snake_i != len(snake)-1:
            snake_i += 1

    arr[hr][hc] = nd
    hr, hc = hr + dy[nd], hc + dx[nd]

    if hr < 0 or hr >= N or hc < 0 or hc >= N:
        break
    if arr[hr][hc] != 4 and arr[hr][hc] != -1:
        break

    if arr[hr][hc] != 4:
        td = arr[tr][tc]
        arr[tr][tc] = -1
        tr, tc = tr + dy[td], tc + dx[td]

    arr[hr][hc] = nd
    ns += 1

ns+=1
print(ns)
