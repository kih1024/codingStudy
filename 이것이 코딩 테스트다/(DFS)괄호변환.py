def reverse(p):
    p = list(p)
    for i in range(len(p)):
        if p[i] == '(':
            p[i] = ')'
        else:
            p[i] = '('
    p = "".join(p)
    return p

def DFS(p):
    count = 0
    if p == "":
        return ""
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        
        if count == 0:
            u = p[:i+1]
            v = p[i+1:]
            break

    # 올바른 문자열
    if u[0] == '(':
        return u + DFS(v)
    # 올바른 문자열 x
    else:
        return "(" + DFS(v) + ")" + reverse(u[1:-1])
 
def solution(p):
    ans = DFS(p)
    print(ans)
    return ans
    
solution(")(")