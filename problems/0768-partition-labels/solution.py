from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = defaultdict(int)
        for c in s:
            if c not in s:
                count[c] = 1
            else:
                count[c] = count[c] + 1
        
        l, r = 0, 0
        ans = []
        while r < len(s) and l < len(s):
            currset = set(s[r])
            while currset and r < len(s):
                currset.add(s[r])
                count[s[r]] -= 1
                if count[s[r]] == 0:
                    currset.discard(s[r])
                r += 1
            ans.append(r - l)
            l = r
        
        return ans



            



