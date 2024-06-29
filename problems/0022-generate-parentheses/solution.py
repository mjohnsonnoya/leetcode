class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backTrack(l, r, s):
            if l == r == n:
                res.append(s)
                return
            if l < n:
                backTrack(l + 1, r, s + '(')
            if r < l:
                backTrack(l, r + 1, s + ')')
        backTrack(0,0,"")
        return res

