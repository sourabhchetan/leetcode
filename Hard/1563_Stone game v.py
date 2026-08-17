class Solution(object):
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # Prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[i][j] = maximum score from interval [i, j]
        dp = [[0] * n for _ in range(n)]

        # left[i][j]:
        # max(dp[i][k] + prefix[k+1])
        # for k from i to j
        left = [[0] * n for _ in range(n)]

        # right[i][j]:
        # max(dp[k][j] - prefix[k])
        # for k from i to j
        right = [[0] * n for _ in range(n)]

        from bisect import bisect_left

        # Base cases: one stone
        for i in range(n):
            left[i][i] = prefix[i + 1]
            right[i][i] = -prefix[i]

        # Process intervals by increasing length
        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                # We need:
                # prefix[k+1] <= / >= half of total
                total_boundary = prefix[i] + prefix[j + 1]

                # q = first prefix position where:
                # 2 * prefix[q] >= total_boundary
                q = bisect_left(
                    prefix,
                    (total_boundary + 1) // 2,
                    i + 1,
                    j + 1
                )

                # ------------------------------------------------
                # Case 1: Left part is strictly smaller
                #
                # k + 1 < q
                # ------------------------------------------------
                if q >= i + 2:
                    dp[i][j] = max(
                        dp[i][j],
                        left[i][q - 2] - prefix[i]
                    )

                # ------------------------------------------------
                # Case 2: Right part is smaller
                #
                # k + 1 >= q
                # ------------------------------------------------
                if q <= j:
                    dp[i][j] = max(
                        dp[i][j],
                        right[q][j] + prefix[j + 1]
                    )

                # ------------------------------------------------
                # Case 3: Both parts are equal
                # ------------------------------------------------
                if q <= j and 2 * prefix[q] == total_boundary:

                    # Keep left
                    dp[i][j] = max(
                        dp[i][j],
                        prefix[q] - prefix[i] + dp[i][q - 1]
                    )

                    # Keep right
                    dp[i][j] = max(
                        dp[i][j],
                        prefix[j + 1] - prefix[q] + dp[q][j]
                    )

                # Update range maximum structures
                left[i][j] = max(
                    left[i][j - 1],
                    dp[i][j] + prefix[j + 1]
                )

                right[i][j] = max(
                    right[i + 1][j],
                    dp[i][j] - prefix[i]
                )

        return dp[0][n - 1]