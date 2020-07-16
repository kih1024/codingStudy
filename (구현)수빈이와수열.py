n = int(input())
li = list(map(int, input().split()))

for i in range(n):
    li[i] = li[i] * (i + 1)
result = [li[0]]
for i in range(1, n):
    result.append(li[i] - li[i - 1])
for i in result:
    print(i, end=" ")

# for i in range(1, n ):
# result.append(li[i]*(i+1)- sum(A))
