class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums):
            if not nums:
                return [[]]
            res = []
            for i in range(len(nums)):
                for p in helper(nums[:i] + nums[i+1:]):
                    res.append([nums[i]] + p)
            
            return res
        return helper(nums)
            
                
            
