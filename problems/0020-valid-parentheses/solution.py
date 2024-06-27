class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'{': '}', '[': ']', '(': ')'}
        for c in s:
            if not stack:
                stack.append(c)
            elif stack[-1] not in mapping:
                stack.append(c)
            elif mapping[stack[-1]] == c:
                stack.pop()
            else:
                stack.append(c)
            
        return not stack
