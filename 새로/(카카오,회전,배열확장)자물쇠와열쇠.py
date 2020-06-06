# https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3
# https://juhee-maeng.tistory.com/32 여기 보고 풀이법 알아냄.
def ck(m, ks, ls):
    for i in range(ks - 1, ks + (ls - 1)):
        for j in range(ks - 1, ks + (ls - 1)):
            if m[i][j] == 0:
                return False
    return True

def rotate90(m):
    nm = [[0] * len(m) for _ in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m)):
            nm[j][len(m) - i - 1] = m[i][j]
    return nm

def inject(m, lock, ks, ls):
    for i in range(ls):
        m[ks - 1 + i][ks - 1 : ks - 1 + ks] = lock[i]

def solution(key, lock):
    answer = True
    ks = len(key)
    ls = len(lock)
    m = [[2 for _ in range(ls + (2 * ks) - 2)] for _ in range(ls + (2 * ks) - 2)]
    inject(m, lock, ks, ls)
    for _ in range(4):
        for i in range(len(m) - (ks - 1)):
            for j in range(len(m) - (ks - 1)):
                for r in range(len(key)):
                    for c in range(len(key)):
                        m[i + r][j + c] = m[i + r][j + c] ^ key[r][c]
                if ck(m, ks, ls):
                    return True
                inject(m, lock, ks, ls)
        key = rotate90(key)

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
