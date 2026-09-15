class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)

        # dp[i] = maximum number of valid palindromes
        # using s[0:i]
        dp = [0] * (n + 1)

        # prev[i] tells whether s[i:j-1] is a palindrome
        prev = [False] * n

        for j in range(n):
            curr = [False] * n

            # We can always skip s[j]
            dp[j + 1] = dp[j]

            for i in range(j, -1, -1):
                # Check whether s[i:j+1] is a palindrome
                if s[i] == s[j] and (j - i <= 2 or prev[i + 1]):
                    curr[i] = True

                    length = j - i + 1

                    if length >= k:
                        dp[j + 1] = max(dp[j + 1], dp[i] + 1)

            prev = curr

        return dp[n]
