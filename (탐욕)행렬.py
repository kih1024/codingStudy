# https://www.acmicpc.net/problem/1080


def reverse(r, c):
    if r + 2 > n - 1 or c + 2 > m - 1:
        return
    for i in range(3):
        for j in range(3):
            arr1[r + i][c + j] ^= 1


def process():
    global count
    for i in range(n):
        for j in range(m):
            if arr1 == arr2:
                return True

            if arr1[i][j] != arr2[i][j]:
                reverse(i, j)
                count += 1
    return False


n, m = map(int, input().split())
arr1 = [list(map(int, list(input()))) for i in range(n)]
arr2 = [list(map(int, list(input()))) for i in range(n)]
count = 0
if not process():
    print(-1)
else:
    print(count)
