class Solution:
    def isValid(self, s: str) -> bool:
        equiv = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif stack[-1] in equiv and equiv[stack[-1]] == c:
                stack.pop()
            else:
                stack.append(c)
        
        return not stack
            
