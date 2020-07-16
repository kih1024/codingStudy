# https://www.acmicpc.net/problem/1439

s = input()
count = [0] * 2

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count[int(s[i])] += 1

count[int(s[-1])] += 1

print(min(count))
