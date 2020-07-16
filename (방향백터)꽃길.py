# https://www.acmicpc.net/status?from_mine=1&problem_id=14620&user_id=kih1024
def check(pos):
    area = []
    sumV = 0
    for i in range(3):
        r = pos[i] // n
        c = pos[i] % n
        if r == 0 or r == n - 1 or c == 0 or c == n - 1:
            return 10000
        for w in range(5):
            dy = r + y[w]
            dx = c + x[w]
            area.append((dy, dx))
            sumV += arr[dy][dx]

    if len(set(area)) == 15:
        return sumV
    else:
        return 10000


n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
y = [0, 0, 1, 0, -1]
x = [0, 1, 0, -1, 0]
result = 10000

for i in range(n * n):
    for j in range(i + 1, n * n):
        for k in range(j + 1, n * n):
            result = min(result, check([i, j, k]))

print(result)
