N, M = list(map(int, input().split(" ")))
li = list(map(int, input().split(" ")))

total = 0
for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if li[i] + li[j] + li[k] <= M:
                total = max(total, li[i] + li[j] + li[k])

print(total)
