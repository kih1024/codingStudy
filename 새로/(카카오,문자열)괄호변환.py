# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3


def ck(p):
    l, r = 0, 0
    for i in range(len(p)):
        if p[i] == "(":
            l += 1
        else:
            r += 1
        if r > l:
            return False
    return True


def reverse(p):
    p = p.replace("(", "l").replace(")", "r").replace("l", ")").replace("r", "(")

    return p


def solution(p):
    l, r = 0, 0
    if p == "":
        return ""
    for i in range(len(p)):
        if p[i] == "(":
            l += 1
        else:
            r += 1
        if l == r:
            break
    u, v = p[: i + 1], p[i + 1 :]
    if ck(u):
        return u + solution(v)
    else:
        uu = list(u)
        uu[0], uu[-1] = "", ""
        u = "".join(uu)
        u = reverse(u)
        return "(" + solution(v) + ")" + u


print(solution("()(())()"))
