class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token == '+':
                b = float(stack.pop())
                a = float(stack.pop())
                stack.append((a + b))
            elif token == '-':
                b = float(stack.pop())
                a = float(stack.pop())
                stack.append((a - b))
            elif token == '*':
                b = float(stack.pop())
                a = float(stack.pop())
                stack.append((a*b))
            elif token == '/':
                b = float(stack.pop())
                a = float(stack.pop())
                stack.append(int(a/b))
            else:
                stack.append(int(token))


        return int((stack[0]))
            
