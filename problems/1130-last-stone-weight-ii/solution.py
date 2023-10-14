class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total_weight = sum(stones)
        dp = [False] * (total_weight//2 + 1)
        dp[0] = True
        max_i = 0
        
        for stone in stones:
            for i in range(total_weight // 2, stone - 1, -1):
                dp[i] = dp[i] or dp[i - stone]
                if dp[i]:
                    max_i = max(max_i, i)
        return total_weight - 2 * max_i
        
        
