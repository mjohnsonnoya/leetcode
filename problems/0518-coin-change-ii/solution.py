class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        
        # Base case initialization
        for i in range(len(coins) + 1):
            dp[i][0] = 1
            
        # Iterate through all coins and all amounts to fill dp array
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i-1][j]  # not use the i-th coin
                if j >= coins[i-1]:  # use the i-th coin
                    dp[i][j] += dp[i][j-coins[i-1]]
        
        return dp[len(coins)][amount]

