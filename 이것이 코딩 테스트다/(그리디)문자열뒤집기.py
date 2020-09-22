arr = list(map(int, input()))
status = [0] * 2
now = -1
for i in arr:
    if i != now:
        status[i] += 1
        now = i

print(min(status))

