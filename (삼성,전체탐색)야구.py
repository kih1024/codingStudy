# https://www.acmicpc.net/problem/17281
# 시간이 너무 빡빡해서 파이썬으로는 무조건 시간초과. pypy3로 해야 하고 변수 하나 차이로 시간초과가 날수가 있음.
# 가급적 코드가 지저분해지더라도 있는 변수 그대로 쓰고 따로 할당하지 말자 그리고 조금의 속도를 위해서 배열 할당은 피한다.

import sys
from itertools import permutations


def process(order):
    hitter_idx = 0
    score = 0
    for i in ininig:
        outC = 0
        b1, b2, b3 = 0, 0, 0
        while outC < 3:
            if i[order[hitter_idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif i[order[hitter_idx]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif i[order[hitter_idx]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif i[order[hitter_idx]] == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            else:
                outC += 1
            hitter_idx = (hitter_idx + 1) % 9
    return score


n = int(sys.stdin.readline())
ininig = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
answer = 0
li = permutations(range(1, 9), 8)
for li in permutations(range(1, 9), 8):
    answer = max(answer, process(list(li[0:3]) + [0] + list(li[3:])))

print(answer)
