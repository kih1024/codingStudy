# def bisec(s, e):
#     global x, pos

#     if e - s == 0 and x == arr[s]:
#         pos = s
#         return True
#     if e - s == 0 and x != arr[s]:
#         return False

#     m = (s + e) // 2
#     if x == arr[m]:
#         pos = m
#         return True
#     else:
#         if x > arr[m]:
#             return bisec(m + 1, e)
#         else:
#             return bisec(s, m - 1)


# N, x = map(int, input().split())
# arr = list(map(int, input().split()))
# pos = 0
# result = bisec(0, N - 1)

# if result:
#     ans = 1
#     for l in range(1, pos):
#         pos_l = pos - l
#         if arr[pos_l] != x:
#             break
#         ans += 1
#     for r in range(1, N - 1 - pos):
#         pos_r = pos + r
#         if arr[pos_r] != x:
#             break
#         ans += 1
#     print(ans)
# else:
#     print(-1)

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x 입력 받기
array = list(map(int, input().split())) # 전체 데이터 입력 받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)