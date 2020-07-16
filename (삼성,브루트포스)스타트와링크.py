from itertools import combinations


def process():
    start = []
    link = []
    sum_s = 0
    sum_l = 0
    for i in range(len(team)):
        if team[i] == 0:
            start.append(i)
        else:
            link.append(i)
    for s, l in list(combinations(start, 2)):
        sum_s = sum_s + arr[s][l] + arr[l][s]
    for s, l in list(combinations(link, 2)):
        sum_l = sum_l + arr[s][l] + arr[l][s]

    return abs(sum_s - sum_l)


n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
minV = 1e9
team = [0] * n
member = [i for i in range(n)]
for i in list(combinations(member, n // 2)):
    team = [0] * n
    for j in range(n // 2):
        team[i[j]] = 1

    result = process()
    minV = min(result, minV)

print(minV)

# # 0 스타트, 1 링크
# 이 함수는 각각 사람이 어느 팀인지 알려주는 team 리스트를 구하기 위해서 사용
# def dfs(depth, now_s, now_l):
#     global minV
#     if depth == n:
#         result = process()
#         minV = min(result, minV)
#         return

#     for i in range(2):
#         if i == 0 and now_s == (n // 2):
#             continue
#         if i == 1 and now_l == (n // 2):
#             break
#         team[depth] = i
#         if i == 0:
#             dfs(depth + 1, now_s + 1, now_l)
#         else:
#             dfs(depth + 1, now_s, now_l + 1)

#     return


# n = int(input())
# arr = [list(map(int, input().split())) for i in range(n)]
# minV = 1e9
# team = [0] * n
# dfs(0, 0, 0)
# print(minV)
