class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        curr = 0
        ans = nums[0]
        r = 0
        while r < len(nums):
            if curr < 0:
                curr = 0
            else:
                curr += nums[r]
                ans = max(curr, ans)
                r += 1
        return ans

            
