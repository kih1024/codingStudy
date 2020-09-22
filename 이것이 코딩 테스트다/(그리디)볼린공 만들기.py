N, M = map(int, input().split())
num = [0] * (M + 1)
arr = list(map(int, input().split()))

for i in arr:
    num[i] += 1

ans = (N * (N - 1)) // 2

for i in range(1, len(num)):
    if num[i] > 1:
        temp = (num[i] * (num[i] - 1)) // 2
        ans -= temp

print(ans)
