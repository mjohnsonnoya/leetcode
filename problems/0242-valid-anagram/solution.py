class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1dict = defaultdict(int)
        s2dict = defaultdict(int)
        for i in range(len(s)):
            s1dict[s[i]] += 1
            s2dict[t[i]] += 1
        
        if s1dict.keys() != s2dict.keys():
            return False

        for key in s1dict.keys():
            if key not in s2dict:
                return False
            elif s1dict[key] != s2dict[key]:
                return False

        return True
