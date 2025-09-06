class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            ans[i] *= prefix
            ans[-(i + 1)] *= postfix
            prefix *= nums[i]
            postfix *= nums[-(i + 1)]
    
        
        return ans
            
