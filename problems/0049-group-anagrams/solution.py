class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] = count[ord(c)-ord('a')] + 1
            res[tuple(count)].append(s)
        for key in res:
            final.append(res[key])
        return final

