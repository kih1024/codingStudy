arr = list(map(int,input()))

ans = 0

for i in range(len(arr)):
    if ans <= 1 or arr[i] <= 1:
        ans += arr[i]
    else:
        ans *= arr[i]

print(ans)