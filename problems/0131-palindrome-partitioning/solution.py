class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            l = 0
            r = len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True
        res = []
        
        def helper(i, vals):
            if i == len(s):
                res.append(vals.copy())
                return
            j = i + 1
            while j <= len(s):
                if isPalindrome(s[i:j]):
                    if vals:
                        vals.append(s[i:j])
                    else:
                        vals = [s[i:j]]
                    helper(j,vals)
                    vals.pop()
                j += 1
        helper(0, [])
        return res
