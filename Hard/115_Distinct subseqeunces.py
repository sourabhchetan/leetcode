class Solution(object):
    def numDistinct(self, s, t):
        n = len(t)

        # dp[j] = number of ways to form t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1

        for char_s in s:
            # Traverse backwards so previous values are not overwritten
            for j in range(n, 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]
