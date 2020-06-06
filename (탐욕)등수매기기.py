# https://www.acmicpc.net/problem/2012
n = int(input())
temp = []
count = 0
for _ in range(n):
    temp.append(int(input()))
temp.sort()

for i in range(n):
    count += abs(temp[i]-(i+1))

print(count)

