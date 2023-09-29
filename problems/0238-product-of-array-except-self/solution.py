class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
                res[i] *= prefix
                res[-(i+1)] *= postfix
                
                prefix *= nums[i]
                postfix *= nums[-(i+1)]
        return res
        
