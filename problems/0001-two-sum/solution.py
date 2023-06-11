class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difdict = {}
        for i,j in enumerate(nums):
            dif = target - j
            if dif in difdict:
                return [difdict[dif],i]
            difdict[j] = i


            
            
