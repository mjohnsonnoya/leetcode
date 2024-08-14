class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def helper(i):
            if i == 0:
                return 0
            if i < 0:
                return float('inf')
            if i in dp:
                return dp[i]
            ans = float('inf')
            for c in coins:
                ans = min(ans, 1 + helper(i - c))

            dp[i] = ans
            return ans
        val = helper(amount)
        if val > 10**4:
            print("this is val: ", val)
            return -1
        else:
            return val

