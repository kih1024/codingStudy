from collections import deque


def dfs(depth, v):
    if depth == -1:
        values.append(v)
        return

    idx = len(temp) - 1 - depth
    for i in temp[idx]:
        v += i * (10 ** depth)
        dfs(depth - 1, v)
        v -= i * (10 ** depth)


N = int(input())
M = int(input())
arr = list(map(int, input().split()))
purpose = []
tn = N
while N != 0:
    t = N % 10
    N = N // 10
    purpose.append(t)

purpose = purpose[::-1]
length = len(purpose)
temp = deque([[] for _ in range(length)])

ans = 0
count = 0
useNumber = True
isAppend = False
for i in range(length):
    if purpose[i] not in arr:
        count += 1
        temp[i].append(purpose[i])
    else:
        for j in range(1, max(purpose[i] + 1, 10 - purpose[i])):
            isFind = False
            for k in [j, -j]:
                if purpose[i] + k < 0 or purpose[i] + k > 10:
                    continue
                purT = (purpose[i] + k) % 10
                if purT == 0 and i == 0:
                    if 0 not in arr and 1 not in arr:
                        temp[i].append(0)
                        isAppend = True
                        isFind = True
                    continue
                if purT not in arr:
                    temp[i].append(purT)
                    isFind = True
            if isFind:
                count += 1
                break

    if len(temp[i]) == 0:
        useNumber = False
        break
if isAppend:
    count += 1
    temp.appendleft([0, 1])
if not useNumber:
    print(abs(tn - 100))
else:
    ans += count
    print(temp)
    values = []
    dfs(len(temp) - 1, 0)
    print(values)
    intervel = 1e9
    for i in values:
        intervel = min(intervel, abs(i - tn))
    ans += intervel
    print(min(ans, abs(tn - 100)))
# # 예외
# 9999
# 1
# 9
# 답: 6 (10000-)

# in:
# 100000
# 9
# 0 1 2 3 4 5 6 7 8

# out:
# 6