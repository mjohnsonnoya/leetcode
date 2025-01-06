class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        for letter in s:
            if letter not in sdict:
                sdict[letter] = 0
            sdict[letter] += 1
        tdict = {}
        for letter in t:
            if letter not in tdict:
                tdict[letter] = 0
            tdict[letter] += 1
        return sdict == tdict
