class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        l = 0
        r = 0
        while (r <= len(s)):
            if (len(set(s[l:r])) != (len(s[l:r]))):
                l +=1
            else:
                maxlength = max(maxlength,(len(s[l:r])))
                r+=1
        return maxlength
