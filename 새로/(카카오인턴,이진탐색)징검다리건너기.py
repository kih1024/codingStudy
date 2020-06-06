def ck(stones, k, midV):
    count = 0
    for i in range(len(stones)):
        if stones[i] < midV:
            count += 1
        else:
            count = 0
        if count >= k:
            return False
    return True


answer = 0

def solution(stones, k):
    global answer
    maxV, minV = max(stones)+1, 1
    while minV < maxV-1:
        # print("asd")
        print(minV,maxV)
        mid = (minV+maxV) // 2
        if ck(stones,k,mid):
            minV = mid
        else:
            maxV = mid
        print(minV,maxV)
        
    return minV


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
