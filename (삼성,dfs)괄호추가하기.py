# https://www.acmicpc.net/source/19290164
def dfs(i,res):
    global maxV
    if i == n:
        maxV = max(maxV,res)
        return
    if li[i] == "+":
        dfs(i+2,res+int(li[i+1]))
        if i == n-2:
            return
        f=int(li[i+1])
        o=li[i+2]
        s=int(li[i+3])

        if o=="+":
            dfs(i+4,res+(f+s))
        elif o=="-":
            dfs(i+4,res+(f-s))
        else:
            dfs(i+4,res+(f*s))
    elif li[i] == "-":
        dfs(i+2,res-int(li[i+1]))
        if i == n-2:
            return
        f=int(li[i+1])
        o=li[i+2]
        s=int(li[i+3])

        if o=="+":
            dfs(i+4,res-(f+s))
        elif o=="-":
            dfs(i+4,res-(f-s))
        else:
            dfs(i+4,res-(f*s))
    else:
        dfs(i+2,res*int(li[i+1]))
        if i == n-2:
            return
        f=int(li[i+1])
        o=li[i+2]
        s=int(li[i+3])

        if o=="+":
            dfs(i+4,res*(f+s))
        elif o=="-":
            dfs(i+4,res*(f-s))
        else:
            dfs(i+4,res*(f*s))

n = int(input())
li = input()
maxV = -1*2**31
dfs(1,int(li[0]))
print(maxV)