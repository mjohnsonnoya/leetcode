class Solution:
    def isPalindrome(self, s, i, j):
        if i < 0 or j >= len(s):
            return False
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
            
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l = i
            r = i
            while self.isPalindrome(s,l,r):
                count += 1
                l-=1
                r+=1
        for i in range(len(s)):
            l = i
            r = i + 1
            while self.isPalindrome(s,l,r):
                count += 1
                l-=1
                r+=1
        return count
                
