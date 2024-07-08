class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        res = []
        def dfs(nums):
            if not nums:
                res.append(stack.copy())
                return
            for i in range(len(nums)):
                stack.append(nums[i])
                dfs(nums[:i] + nums[i+1:])
                stack.pop()
        dfs(nums)
        return res
            

