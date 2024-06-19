class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        word = set()
        max_count = 0
        while r < len(s):
            if s[r] in word:
                while s[l] != s[r]:
                    word.remove(s[l])
                    l += 1
                l += 1
            word.add(s[r])
            max_count = max(max_count, r - l + 1)
            r += 1
        
        return max_count


