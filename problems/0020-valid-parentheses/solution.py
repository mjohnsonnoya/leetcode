class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'{': '}', '[': ']', '(': ')'}
        for char in s:
            if char in parentheses:
                stack.append(char)
            elif stack and parentheses[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return len(stack) == 0

