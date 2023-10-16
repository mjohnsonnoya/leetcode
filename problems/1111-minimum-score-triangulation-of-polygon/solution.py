class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        # Initialize a 2D dp array with all values set to 0.
        dp = [[0] * n for _ in range(n)]

        # Iterate through all sub-polygons of length 3 to n.
        for length in range(3, n+1):
            # Iterate through all possible starting vertices for the sub-polygon.
            for i in range(n-length+1):
                # The ending vertex of the sub-polygon.
                j = i + length - 1
                # Initialize dp[i][j] with a large number since we want to minimize it.
                dp[i][j] = float('inf')
                # Iterate through all possible intermediate vertices k to form a triangle (i, k, j).
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[j] * values[k])

        # The minimum score to triangulate the entire polygon is stored in dp[0][n-1].
        return dp[0][n-1]
