class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def dfs(i, amount):
            if i >= len(nums):
                return 1 if amount == target else 0
            if (i, amount) in cache:
                return cache[(i,amount)]
            cache[(i, amount)] = dfs(i + 1, amount + nums[i]) + dfs(i+1, amount - nums[i])
            return cache[(i,amount)]
        return dfs(0,0)
                
