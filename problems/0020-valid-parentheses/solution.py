class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        equiv = {'(': ')', '{': '}', '[':']'}
        for char in s:
            if not stack:
                stack.append(char)
            elif stack[-1] in equiv and equiv[stack[-1]] == char:
                stack.pop()
            else:
                stack.append(char)
        return not stack

