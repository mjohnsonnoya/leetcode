class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        cache = {}
        
        def helper(i, j, isPlayer1):
            if i > j:
                return 0
            if (i, j, isPlayer1) in cache:
                return cache[(i, j, isPlayer1)]
            if i == j:
                if isPlayer1:
                    cache[(i,j,isPlayer1)] = nums[i]
                else:
                    cache[(i,j,isPlayer1)] = -nums[i]
                    
            if isPlayer1:
                start = nums[i] + helper(i + 1, j, not isPlayer1)
                end = nums[j] + helper(i, j - 1, not isPlayer1)
                cache[(i, j, isPlayer1)] = max(start, end)
            
            else:
                start = -nums[i] + helper(i + 1, j, not isPlayer1)
                end = -nums[j] + helper(i, j - 1, not isPlayer1)
                cache[(i, j, isPlayer1)] = min(start, end)
            
            return cache[(i, j, isPlayer1)]
        return helper(0, len(nums) - 1, True) >= 0
        
