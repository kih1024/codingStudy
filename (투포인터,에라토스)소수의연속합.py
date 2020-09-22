N = int(input())
p = []
ck = [False] * (N + 1)
end = 0
summary = 0
ans = 0
for i in range(2, N + 1):
    if not ck[i]:
        p.append(i)
        t = i + i
        for j in range(t, N + 1, i):
            ck[j] = True
size = len(p)
for start in range(size):
    while summary < N and end < size:
        summary += p[end]
        end += 1

    if summary == N:
        ans += 1
    summary -= p[start]
print(ans)

