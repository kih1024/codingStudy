n = int(input())
sec = 0
now = 0
rate = 0

while now < n:
    sec += 1
    rate += 1

    if now + rate > n:
        rate = 1
        now += rate
    else:
        now += rate
print(sec)
