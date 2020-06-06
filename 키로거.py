test_case = int(input())
for _ in range(test_case):
    lefts = []
    rights = []
    pivot = 0
    pw = input()
    for i in range(len(pw)):
        if pw[i] == '<':
            if len(lefts) != 0:
                rights.append(lefts.pop())
        elif pw[i] == '>':
            if len(rights) != 0:
                lefts.append(rights.pop())
        elif pw[i] == '-':
            if len(lefts) != 0:
                lefts.pop()
        else:
            lefts.append(pw[i])
    lefts.extend(reversed(rights))
    print(''.join(lefts))
