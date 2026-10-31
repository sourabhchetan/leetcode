class Solution(object):
    def uniquePaths(self, grid):
        MOD = 10**9 + 7

        m, n = len(grid), len(grid[0])

        # Paths arriving from above
        dp = [1] + [0] * (n - 1)

        for i in range(m):
            # Paths arriving from the left
            left = 0

            for j in range(n):
                if grid[i][j] == 1:
                    # Mirror: swap incoming directions
                    left, dp[j] = dp[j], left

                else:
                    # Empty cell: combine both incoming paths
                    ways = (left + dp[j]) % MOD

                    # Send paths in both directions
                    left = ways
                    dp[j] = ways

        return left
