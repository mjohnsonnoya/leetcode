class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        word = set(s[l])
        max_len = 1
        while r < len(s):
            if s[r] in word:
                while s[l] != s[r]:
                    word.remove(s[l])
                    l += 1
                word.remove(s[l])
                l += 1
            
            else:
                word.add(s[r])
                r += 1
            max_len = max(len(word), max_len)
        
        return max_len
