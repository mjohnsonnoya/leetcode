class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsdict = {}
        for i in nums:
            if i in numsdict:
                return True
            else:
                numsdict[i] = 1
        return False
