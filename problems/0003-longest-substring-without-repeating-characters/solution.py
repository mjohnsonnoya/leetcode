class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubstring = 0
        l,r = 0,0
        substringSet = set()
        if not s:
                return maxSubstring
        while r < len(s):
                if s[r] not in substringSet:
                        substringSet.add(s[r])
                        maxSubstring = max(maxSubstring, r - l + 1)
                        r+=1
                else:
                        substringSet.remove(s[l])
                        l +=1
        return maxSubstring
