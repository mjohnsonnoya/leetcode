class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            #res = {}
            res = defaultdict(list)
            final = []
            for s in strs:
                count = [0] * 26
                for c in s:
                    i = (ord(c) - ord("a"))
                    count[i] += 1
                res[tuple(count)].append(s)
            for key in res:
                final.append(res[key])
            return final
