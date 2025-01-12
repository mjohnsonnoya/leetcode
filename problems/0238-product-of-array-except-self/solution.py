class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = nums[0]
        for i in range(1, len(nums)):
            ans[i] *= prefix
            prefix *= nums[i]
        postfix = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans




