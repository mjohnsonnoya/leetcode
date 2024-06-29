class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        res = []
        
        def s_to_dict(s):
            freq = {}
            for c in s:
                freq[c] = freq.get(c,0) + 1
            return freq

        for s in strs:
            freq = s_to_dict(s)
            sorted_tuple = tuple(sorted(freq.items())) 
            if sorted_tuple in groups:
                groups[sorted_tuple].append(s)
            else:
                groups[sorted_tuple] = [s]

        print(groups)
        for anagram in groups:
            res.append(groups[anagram])
        
        return res


