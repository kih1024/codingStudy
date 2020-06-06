# # https://www.acmicpc.net/problem/14503


def process(r, c, d):
    rr, cc, dd = r, c, d
    count = 0
    while True:
        isAll = True
        if arr[rr][cc] == 0:
            arr[rr][cc] = 2
            count += 1
        for i in range(4):
            if arr[rr + y[(dd - 1) % 4]][cc + x[(dd - 1) % 4]] == 0:
                dd = (dd - 1) % 4
                rr = rr + y[dd]
                cc = cc + x[dd]
                isAll = False
                break
            else:
                dd = (dd - 1) % 4
        # 네방향 다 이동 못하면 반대로 이동
        if isAll:
            if arr[rr + y[(dd - 2) % 4]][cc + x[(dd - 2) % 4]] == 1:
                return count
            rr = rr + y[(dd - 2) % 4]
            cc = cc + x[(dd - 2) % 4]


n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
y, x = [-1, 0, 1, 0], [0, 1, 0, -1]
result = process(r, c, d)
print(result)
