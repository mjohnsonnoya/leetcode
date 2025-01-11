class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramdict = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in anagramdict:
                anagramdict[key] = []
            anagramdict[key].append(word)
        ans = []
        for key, val in anagramdict.items():
            ans.append(val)
        return ans
        
            
