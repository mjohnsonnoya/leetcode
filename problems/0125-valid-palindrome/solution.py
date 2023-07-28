class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')) or (ord('0') <= ord(c) <= ord('9'))]
        indices = range(len(s))
        k = len(indices)
        h = int(k //2)
        for i in indices[:h]:
            if s[i].lower() != s[len(s) - i -1].lower():
                return False
        return True
                
