import sys
# 파이썬은 1초에 2천만 연산
# 입력수가 엄청 많기 때문에(1~10000000) 평범하게 정렬 알고리즘 쓰면 안된다. nlog(n)연산이라 시간초과
# 따라서 계수정렬(counting sorting) 알고리즘 씀
# 값의 갯수를 해당값에 해당하는 인덱스에 저장
# 입력수가 많을때는 속도가 빠른 readline을 써준다.

n = int(sys.stdin.readline())

li = 10001 * [0]

for _ in range(n):
    t = int(sys.stdin.readline())
    li[t] += 1

for i in range(1, 10001):
    if li[i] != 0:
        for _ in range(li[i]):
            print(i)

