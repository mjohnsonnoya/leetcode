class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            elif token == "+":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 + val2)
            elif token == "-":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 - val2)
            elif token == "*":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 * val2)
            elif token == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(val1 / val2))
        return stack[0]



