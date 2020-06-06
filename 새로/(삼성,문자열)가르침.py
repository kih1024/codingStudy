from itertools import combinations
# SET 은 + ,- ,|,& 연산이 가능함!
words = []
N,K = map(int,input().split())
base = set("antic")
check = set()
for n in range(N):
    s = input()
    s = set(s[4:-4]) - base
    check = check | s
    words.append(s)

if K < 5:
    print(0)
    exit(0)
if K == 26:
    print(N)
    exit(0)

select = min(K-5,len(check))
know = list(combinations(check,select))
ans = 0

for kw in know:
    count = 0
    kw = set(kw)
    for w in words:
        if len(w - kw) == 0:
            count += 1
    ans = max(ans,count)

print(ans)