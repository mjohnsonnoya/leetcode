class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        visited = set()
        l, r = 0, 0
        maxlen = 1
        while r < len(s):
            if s[r] in visited:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1
            visited.add(s[r])
            maxlen = max(maxlen, r - l + 1)
            r += 1
        
        return maxlen
        
                
            
