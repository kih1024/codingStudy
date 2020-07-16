n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for i in range(n):
    temp = a[i] - b
    if temp > 0:
        v, r = divmod(temp, c)
        if r > 0:
            answer = answer + v + 2
        else:
            answer = answer + v + 1
    else:
        answer += 1

print(answer)
