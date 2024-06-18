class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r = 0, len(s1) - 1
        s1_chars = [0] * 26
        s2_chars = [0] * 26
        
        for c in s1:
            s1_chars[ord(c) - ord("a")] += 1
        for c in s2[l:r+1]:
            s2_chars[ord(c) - ord("a")] += 1

        while r < len(s2):
            if s1_chars == s2_chars:
                return True
            s2_chars[ord(s2[l]) - ord("a")] -= 1
            l += 1
            r+=1
            if r >= len(s2):
                break
            s2_chars[ord(s2[r]) - ord("a")] += 1
        return False

