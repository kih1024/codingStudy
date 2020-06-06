def solution(gems):
    answer = []
    li = dict()
    dp = [0]*len(gems)
    for n in gems:
        if n not in li:
            li[n] = False
    print(li)
    for s in range(len(gems)-1):
        count 
        for e in range(s+1,len(gems)):
            
        if not li[gems[i]]:
            li[gems[i]] = True
        

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))


n = int(input())

maxI = 1
# dp[i] i번째 수를 마지막 원소로 가지는 lis의 최대길이
dp = [1] * n
li = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            if dp[i] < dp[j] + 1:   
                dp[i] = dp[j] + 1   
                maxI = max(dp[i], maxI) 

print(maxI)