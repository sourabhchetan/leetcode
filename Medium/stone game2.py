class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)

        # suffix[i] = sum of piles[i:]
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp[i][M] = maximum stones current player can get
        # starting at i with M
        dp = [[0] * (n + 2) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):

                # Can take all remaining piles
                if i + 2 * M >= n:
                    dp[i][M] = suffix[i]
                    continue

                best = 0

                for X in range(1, 2 * M + 1):
                    taken = suffix[i] - suffix[i + X]

                    opponent = dp[i + X][max(M, X)]

                    best = max(best, taken + suffix[i + X] - opponent)

                dp[i][M] = best

        return dp[0][1]