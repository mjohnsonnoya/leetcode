class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            tmp = second
            second = max(second, first + nums[i])
            first = tmp
        
        return second
        
