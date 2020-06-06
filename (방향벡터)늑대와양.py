r, c = map(int, input().split())
arr = [list(input()) for i in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
check = True
for i in range(r):
    for j in range(c):
        if arr[i][j] == "W":
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < r and 0 <= x < c:
                    if arr[y][x] == ".":
                        arr[y][x] = "D"
                    if arr[y][x] == "S":
                        check = False
        if arr[i][j] == ".":
            arr[i][j] = "D"

if not check:
    print(0)
else:
    print(1)
    for i in range(len(arr)):
        print("".join(arr[i]))
