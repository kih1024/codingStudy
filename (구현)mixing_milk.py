vol = [0] * 3
nowL = [0] * 3

for i in range(3):
    volume, now = map(int, input().split())
    vol[i] = volume
    nowL[i] = now

for i in range(100):
    temp = min(vol[(i + 1) % 3] - nowL[(i + 1) % 3], nowL[i % 3])
    nowL[i % 3] -= temp
    nowL[(i + 1) % 3] += temp

for i in nowL:
    print(i)
