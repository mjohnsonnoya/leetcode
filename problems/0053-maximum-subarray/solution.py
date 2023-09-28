class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxglobal = float('-inf')
        maxcurrent = float('-inf')
        for i,x in enumerate(nums):
            maxcurrent = max(maxcurrent + x, x)
            maxglobal = max(maxglobal,maxcurrent)
        return maxglobal


