s = input()
f = input()
i = 0
n = 0

while len(s) - i >= len(f):
    if s[i : i + len(f)] == f:
        i = i + len(f)
        n += 1
    else:
        i += 1
print(n)
