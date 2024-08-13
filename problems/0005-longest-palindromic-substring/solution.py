class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(ans):
                    ans = s[l:r+1]
                l -= 1
                r += 1
            
        for i in range(1, n):
            l, r = i - 1, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(ans):
                    ans = s[l:r+1]
                l -= 1
                r += 1
        
        return ans


