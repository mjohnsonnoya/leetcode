class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[\W_]', '', s)
        indices = range(len(s))
        k = len(indices)
        h = int(k //2)
        for i in indices[:h]:
            if s[i].lower() != s[len(s) - i -1].lower():
                return False
        return True
                
