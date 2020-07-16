# https://www.acmicpc.net/problem/16676

n = input()
s = "1" * len(n)
if len(n) == 1:
    print(len(n))
elif int(n) >= int(s):
    print(len(n))
else:
    print(len(n) - 1)
# def countDigit(num):
#     count = 0
#     while num:
#         count += 1
#         num = num // 10
#     return count


# def process():
#     n = int(input())
#     if n == 0:
#         print(1)
#         return
#     count = countDigit(n)
#     bound = 0
#     for i in range(count):
#         bound += 10 ** i
#     if n >= bound:
#         print(count)
#     else:
#         print(count - 1)


# process()
