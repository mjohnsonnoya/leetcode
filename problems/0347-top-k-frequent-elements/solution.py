class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = []
        countdict = {}
        for i in nums:
            countdict[i] = countdict.get(i,0) + 1
        countlist = [[] for i in range(len(nums) + 1)]
        for n, c in countdict.items():
            countlist[c].append(n)
        for i in range(len(countlist) - 1, 0, -1):
            for n in countlist[i]:
                final.append(n)
                if len(final) == k:
                    return final

