s = input()
alph = []
digit = 0
for i in s:
    if i.isalpha():
        alph.append(i)
    else:
        digit += int(i)
alph.sort()
print("".join(alph) + str(digit))
