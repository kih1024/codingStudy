# https://www.acmicpc.net/problem/5585
n = int(input())
rest = 1000 - n
count = 0
for i in [500,100,50,10,5,1]:
    count += rest // i
    rest %= i

print(count)
