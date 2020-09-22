N, M = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, 0
summary = 0
result = 0
for start in range(N):
    while summary < M and end < N:
        summary += arr[end]
        end += 1

    if summary == M:
        result += 1
    summary -= arr[start]

print(result)