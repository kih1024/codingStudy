# https://www.acmicpc.net/problem/14890
# 생각해볼 예제  : 333222333
# 1. 자기 위치의 값보다 큰곳이 두방향 일때는 (length - 2L >=0) 으면 다음거 검사
# 2. 자기 위치의 값보다 큰곳이 한방향 일때는  (length - L >=0) 으면 다음거 검사
# 3. 자기 위치의 값보다 큰곳이 없다면 그냥 다음거 검사
def simulation(arr):
    global result
    count = 0
    before = arr[0]
    length = 0
    for i in range(N):
        if before == arr[i]:
            length += 1
        else:
            if abs(before - arr[i]) >= 2:
                return
            if arr[i] > before:
                count += 1
            if length - count * L < 0:
                return
            else:
                length = 1
                count = 0
            if arr[i] < before:
                count += 1
        before = arr[i]
    if length - count * L < 0:
        return
    # print(arr)
    result += 1
    return


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

for i in arr:
    simulation(i)
#  전치 행렬이용해서 열단위를 행단위로 바꿔서 계산
print(*arr)
print([t for t in zip(*arr)])
arr = [[element for element in t] for t in zip(*arr)]

for i in arr:
    simulation(i)

print(result)
