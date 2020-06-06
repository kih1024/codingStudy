# https://www.acmicpc.net/problem/1439
s = input()
one = 0
zero = 0
if s[0] == "0":
    zero += 1
else:
    one += 1
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        if s[i] == "0":
            zero += 1
        else:
            one += 1

if one>zero:
    print(zero)
else:
    print(one)
