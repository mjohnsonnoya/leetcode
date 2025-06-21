class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            products[i] *= prefix
            products[-1 - i] *= postfix
            prefix *= nums[i]
            postfix *= nums[-1 - i]

        return products
