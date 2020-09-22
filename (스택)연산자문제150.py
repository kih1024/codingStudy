class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i[-1] not in "+-*/":
                stack.append(int(i))
            else:
                f = stack.pop()
                t = stack.pop()
                
                if i == "+":
                    ans = t+f
                elif i == "-":
                    ans = t-f
                elif i == "*":
                    ans = t*f
                else:
                    ans = int(t/f)
                stack.append(ans)
                
        return stack[-1]
                
            