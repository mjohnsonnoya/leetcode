class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            i = 0
            while i < len(prefix) and i < len(s):
                if s[i] == prefix[i]:
                    i += 1
                else:
                    break
            prefix = s[:i]      
        return prefix          


