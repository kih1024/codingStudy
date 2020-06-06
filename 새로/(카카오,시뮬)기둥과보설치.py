# 0 기둥 1 보
# 0 삭제 1 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061?language=python3
# set + tuple로 하는게 add나 remove 할때 빠름,list는 느림.
# 참고 : https://m.post.naver.com/viewer/postView.nhn?volumeNo=26959882&memberNo=33264526
def ck(result):
    for x, y, what in result:
        if what == 0:
            if (
                y == 0
                or (x - 1, y, 1) in result
                or (x, y, 1) in result
                or (x, y - 1, 0) in result
            ):
                continue
            else:
                return False
        elif what == 1:
            if (
                (x, y - 1, 0) in result
                or (x + 1, y - 1, 0) in result
                or ((x - 1, y, 1) in result and (x + 1, y, 1) in result)
            ):
                continue
            else:
                return False
    return True
    

def solution(n, build_frame):
    result = set()
    for x, y, what, how in build_frame:
        if how == 1:
            result.add((x, y, what))
            if not ck(result):
                result.remove((x, y, what))
        else:
            result.remove((x, y, what))
            if not ck(result):
                result.add((x, y, what))

    result = sorted([list(i) for i in result])
    print(result)
    return result


solution(
    5,
    [
        [0, 0, 0, 1],
        [2, 0, 0, 1],
        [4, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [2, 1, 1, 1],
        [3, 1, 1, 1],
        [2, 0, 0, 0],
        [1, 1, 1, 0],
        [2, 2, 0, 1],
    ],
)

# i = set()
# i.add((4,2))
# i.add((2,99))
# i.add((5,3))
# print(i)
