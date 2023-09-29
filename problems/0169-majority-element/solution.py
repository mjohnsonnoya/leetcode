class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxfreq = 0
        maxelem = None
        freqdict = {}
        for i in nums:
                freqdict[i] = freqdict.get(i,0) + 1
                if freqdict[i] > maxfreq:
                        maxfreq = freqdict[i]
                        maxelem = i
        return maxelem
                
        
