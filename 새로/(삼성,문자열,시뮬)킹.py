K, S, N = input().split()

kr, kc = 8 - int(K[1:]), int(ord(K[0])) - 65
sr, sc = 8 - int(S[1:]), int(ord(S[0])) - 65

move = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1)
}
for _ in range(int(N)):
    a = input()
    dy, dx = move[a]
    y = kr + dy
    x = kc + dx
    if y < 0 or y >= 8 or x < 0 or x >= 8:
        continue
    if y == sr and x == sc:
        ys = sr + dy
        xs = sc + dx
        if ys < 0 or ys >= 8 or xs < 0 or xs >= 8:
            continue
        kr, kc, sr, sc = y, x, ys, xs
    else:
        kr, kc = y, x

print(chr(kc + 65) + str(8 - kr))
print(chr(sc + 65) + str(8 - sr))
