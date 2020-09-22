def ck(result):
    for x, y, a in result:
        # 0 보 1 기둥
        if a == 1:
            if (
                (x, y - 1, 0) in result
                or (x + 1, y - 1, 0) in result
                or ((x - 1, y, 1) in result and (x + 1, y, 1) in result)
            ):
                continue
            else:
                return False
        # 기둥
        else:
            if y == 0 or (x-1,y,1) in result or (x,y,1) in result or (x,y-1,0) in result:
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    result = set()
    for x, y, a, b in build_frame:
        if b == 1:
            result.add((x, y, a))
            if not ck(result):
                result.remove((x, y, a))
        else:
            result.remove((x, y, a))
            if not ck(result):
                result.add((x, y, a))

    result = sorted([list(i) for i in result])
    return result
