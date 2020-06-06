import sys

n = int(input())
k = int(input())

# 집중국의 개수가 n 이상일때
if k >= n:
    print(0)
    sys.exit()
    
arr = list(map(int, input().split()))
h = []
result = 0
arr.sort()
for i in range(len(arr) - 1):
    temp = arr[i + 1] - arr[i]
    h.append(temp)

h.sort(reverse=True)

for i in range(k - 1):
    h[i] = 0

for i in h:
    result += i

print(result)
