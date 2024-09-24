class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(res, nums):
            if not nums:
                ans.append(res.copy(
                    
                ))
            for idx in range(len(nums)):
                res.append(nums[idx])
                helper(res, nums[:idx] + nums[idx + 1:])
                res.pop()
        
        helper([], nums)
        return ans

