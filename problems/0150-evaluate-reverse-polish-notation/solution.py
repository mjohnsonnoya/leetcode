class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == '+':
                    stack.append(str(num1 + num2))
                if token == '-':
                    stack.append(str(num1 - num2))
                if token == '*':
                    stack.append(str(num1 * num2))
                if token == '/':
                    stack.append(str(int(num1 / num2)))
        return int(stack[0])
        
