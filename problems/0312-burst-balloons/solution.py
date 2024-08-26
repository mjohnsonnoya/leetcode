class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]  # Add virtual balloons
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for l in range(1, n + 1):  # length of the subarray
            for i in range(1, n - l + 2):  # start of the subarray
                j = i + l - 1  # end of the subarray
                for k in range(i, j + 1):  # assume k is the last balloon to burst
                    # Calculate coins if k is the last balloon to burst
                    coins = dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k + 1][j]
                    dp[i][j] = max(dp[i][j], coins)

        return dp[1][n]



