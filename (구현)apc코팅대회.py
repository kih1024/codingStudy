# https://www.acmicpc.net/problem/17224
n, l, k = map(int, input().split())
easy, hard = 0, 0

for i in range(n):
    sub1, sub2 = map(int, input().split())
    if sub2 <= l:
        hard += 1
    elif sub1 <= l:
        easy += 1

# hard 문제
result = min(hard, k) * 140

# easy
if hard < k:
    result += min(k - hard, easy) * 100

print(result)


# n, l, k = map(int, input().split())
# problems = []
# count = 0
# result = 0
# solve = [False] * n
# for i in range(n):
#     low, high = map(int, input().split())
#     problems.append((low, high))

# # 어려운 문제까지 풀수 있는 문제를 먼저 샌다.
# if count < k:
#     for i in range(n):
#         if solve[i] == False and problems[i][1] <= l:
#             solve[i] = True
#             count += 1
#             result += 140
#             if count >= k:
#                 break

# if count < k:
#     for i in range(n):
#         if solve[i] == False and problems[i][0] <= l:
#             count += 1
#             result += 100
#             if count >= k:
#                 break

# print(result)
