from collections import deque


def ck(m, kl, ll):
    for i in range(kl - 1, kl + (ll - 1)):
        for j in range(kl - 1, kl + (ll - 1)):
            if m[i][j] == 0:
                return False
    return True


def rotate(m):
    length = len(m)
    nm = [[0] * length for _ in range(length)]

    for r in range(length):
        for c in range(length):
            nm[c][length - r - 1] = m[r][c]
    return nm


def inject(m, lock, kl, ll):
    for i in range(ll):
        m[kl - 1 + i][kl - 1 : kl - 1 + kl] = lock[i]


def solution(key, lock):
    kl, ll = len(key), len(lock)
    m = [[1 for _ in range(ll + (2 * kl) - 2)] for _ in range(ll + (2 * kl) - 2)]
    inject(m, lock, kl, ll)
    for _ in range(4):
        for i in range(len(m) - (kl - 1)):
            for j in range(len(m) - (kl - 1)):
                for r in range(len(key)):
                    for c in range(len(key)):
                        m[i + r][j + c] = m[i + r][j + c] ^ key[r][c]
                if ck(m, kl, ll):
                    return True
                inject(m, lock, kl, ll)
        key = rotate(key)

    return False
