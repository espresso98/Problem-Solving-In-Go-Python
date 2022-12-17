# O(N), O(N)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op not in ("+", "-", "*", "/"):
                stack.append(int(op))
            else:
                n2 = stack.pop()
                n1 = stack.pop()

                if op == "+":
                    stack.append(n1 + n2)
                elif op == "-":
                    stack.append(n1 - n2)
                elif op == "*":
                    stack.append(n1 * n2)
                elif op == "/":
                    stack.append(int(n1 / n2))
        
        return stack.pop()
        

class Solution2:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = {'-': lambda b, a: a - b, 
               '+': lambda b, a: a + b, 
               '/': lambda b, a: int(a / b), 
               '*': lambda b, a: a * b}

        for op in tokens: 
            st.append(ops[op](st.pop(), st.pop()) if op in ops else int(op))
        return st.pop()  
