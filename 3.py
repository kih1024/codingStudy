from itertools import combinations


def process(road):
    dp = [0] * (len(road))
    if road[0] == "1":
        dp[0] = 1
    for i in range(1, len(road)):
        if road[i] == "1":
            dp[i] = dp[i - 1] + 1

    return max(dp)


def solution(road, n):
    roadT = list(road)
    # print(road)
    count = n
    idx = []
    answer = []
    for i in range(len(road)):
        if road[i] == "0":
            idx.append(i)
    n = min(n, len(idx))
    temp = list(combinations(idx, n))
    for i in temp:
        roadT = list(road)
        for j in i:
            roadT[j] = "1"
        answer.append(process(roadT))

    return max(answer)


solution("111011110011111011111100011111", 3)
