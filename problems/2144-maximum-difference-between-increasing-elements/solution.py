class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        MAX = [min(nums)] * len(nums)
        MAX[-1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            MAX[i] = max(MAX[i + 1], nums[i])
        MIN = [nums[0]]
        for i in range(1, len(nums)):
            MIN.append(min(MIN[i - 1], nums[i]))
        
        max_drawdown = -1
        for i in range(len(nums)):
            if MAX[i] > MIN[i]:
                max_drawdown = max(max_drawdown, MAX[i] - MIN[i])
        
        return max_drawdown
        
            
            
        
