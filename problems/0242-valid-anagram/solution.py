class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = defaultdict(int)
        tdict = defaultdict(int)
        
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sdict[s[i]] += 1
            tdict[t[i]] += 1
        return tdict == sdict
        return True
