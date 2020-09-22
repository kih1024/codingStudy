N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
i = 0
group = 1
print(arr)
while i < len(arr):
    if group == arr[i]:
        ans += 1
        group = 1
    else:
        group += 1
    i += 1

print(ans)

