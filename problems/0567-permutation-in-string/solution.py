class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_list = [0] * 26
        s2_list = [0] * 26
        l, r = 0, len(s1)
        for char in s1:
            s1_list[ord(char) - ord('a')] += 1

        for char in s2[l:r]:
                s2_list[ord(char) - ord('a')] += 1
        
        while r < len(s2):
            if s1_list == s2_list:
                return True
            else:
                s2_list[ord(s2[l]) - ord('a')] -= 1
                s2_list[ord(s2[r]) - ord('a')] += 1
                l += 1
                r += 1
        if s1_list == s2_list:
                return True
        return False
                

        

        
