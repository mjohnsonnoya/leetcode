class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {'(':')','{':'}','[':']'}
        for i in s:
            if i in pMap:
                stack.append(i)
            elif stack and i == pMap[stack[-1]]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
