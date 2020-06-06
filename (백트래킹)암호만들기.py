import copy
import sys

input = sys.stdin.readline


def dfs(arr, pos):
    if len(arr) == l:
        result.append(copy.deepcopy(arr))
        return

    for i in range(pos, len(s)):
        if s[i] not in visit:
            visit.append(s[i])
            arr.append(s[i])
            dfs(arr, i + 1)
            visit.pop()
            arr.pop()


l, c = map(int, input().split())
s = list(input().split())
vowel = ["a", "e", "i", "o", "u"]
visit = []
s.sort()
result = []
arr = []
dfs(arr, 0)

for i in result:
    m = 0
    j = 0
    for j in i:
        if j in vowel:
            m += 1
    if m >= 1 and l - m >= 2:
        print("".join(i))

# # # 이 dfs는 itertools import combination 을 쓰면 간단히 해결 가능하다.
# def dfs(now, start):
#     if len(now) == l:
#         result.append(copy.deepcopy(now))
#         return

#     for i in range(start, len(arr)):
#         if i in visit:
#             continue
#         now.append(arr[i])
#         visit.append(i)
#         dfs(now, i + 1)
#         now.pop()
#         visit.pop()


# vowels = ("a", "e", "i", "o", "u")
# l, c = map(int, input().split())
# arr = input().split()
# result = []
# visit = []
# arr.sort()
# string = []
# dfs(string, 0)

# for password in result:
