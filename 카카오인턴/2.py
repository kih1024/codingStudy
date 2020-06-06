from itertools import permutations
from copy import deepcopy


def dfs(r,num,oper):
    global answer
    if len(r) == 0:
        answer = max(answer,abs(num[0]))
        return    
    op = r.pop(0)
    result = 0
    new_num = deepcopy(num)
    new_oper = deepcopy(oper)
    i = 0
    while i < len(new_oper):
        if new_oper[i] == op:
            print("asd")
            if op == "+":
                temp = new_num[i] + new_num[i+1]
            elif op == "-":
                temp = new_num[i] - new_num[i+1]
            else:
                temp = new_num[i] * new_num[i+1]
            
            new_num[i] = temp
            del new_oper[i]
            del new_num[i+1]
        else:
            i+=1

    dfs(r,new_num,new_oper)
            





answer = 0
def solution(expression):
    global answer
    oper = []
    num = expression.replace("-"," ").replace("+"," ").replace("*"," ")
    num = list(map(int,num.split(" ")))
    for e in expression:
        if e == "+":
            oper.append("+")
        elif e == "-":
            oper.append("-")
        elif e == "*":
            oper.append("*")
    rule = list(permutations(set(oper),len(set(oper))))
    for r in rule:
        dfs(list(r),num,oper)

    return answer

print(solution("100-200*300-500+20"))