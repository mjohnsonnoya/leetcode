class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        if n == 1:
            return 1
        
        first, second = 1, 1
        for i in range(1, n):
            current = 0
            if s[i] != '0':
                current = second
            if 10 <= int(s[i-1: i+1]) <= 26:
                current += first
            first, second = second, current
        
        return current
