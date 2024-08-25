class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, amount):
            if i >= len(nums):
                if amount == target:
                    return 1
                else: return 0
            if (i, amount) in memo:
                return memo[(i, amount)]
            ans = dfs(i + 1, amount - nums[i]) + dfs(i + 1, amount + nums[i])
            memo[(i, amount)] = ans
            return ans
        return dfs(0, 0)
            
                
