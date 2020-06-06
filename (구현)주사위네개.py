# https://www.acmicpc.net/problem/2484
def dice():
    li = sorted(list(map(int, input().split())))
    temp = set(li)
    if len(temp) == 1:
        return li[0] * 5000 + 50000
    elif len(temp) == 2 and li[1] == li[2]:
        return li[1] * 1000 + 10000
    elif len(temp) == 2 and li[1] != li[2]:
        return (li[1] * 500) + (li[2] * 500) + 2000
    elif len(temp) == 3:
        for i in range(3):
            if li[i] == li[i + 1]:
                return li[i] * 100 + 1000
    else:
        return li[-1] * 100


n = int(input())
# money = []

# for i in range(n):
#     li = sorted(list(map(int, input().split())))
#     money.append(dice())

# print(max(money))

print(max(dice() for i in range(n)))