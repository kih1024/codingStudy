N = list(map(int,input()))
left,right = 0,0
for i in range(len(N)//2):
    left += N[i]
for i in range(len(N)//2,len(N)):
    right += N[i]

if left == right:
    print("LUCKY")
else:
    print("READY")
    