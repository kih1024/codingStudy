# https://www.acmicpc.net/problem/9205


def floydWarshall():
    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                m[i][j] = min(m[i][k] + m[k][j], m[i][j])

t = int(input())

for _ in range(t):
    n = int(input())
    p = [list(map(int, input().split())) for i in range(n + 2)]
    m = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                m[i][j] = 0
                continue
            if abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1]) <= 1000:
                m[i][j] = abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1])
            else:
                m[i][j] = 1e9
    # for i in m:
    #     print(i)
    floydWarshall()
    # for i in m:
    #     print(i)

    if m[0][-1] != 1e9:
        print("happy")
    else:
        print("sad")
