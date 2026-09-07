class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7

        # dp = number of distinct subsequences including empty string
        dp = 1

        # Stores dp value before the previous occurrence of each character
        last = {}

        for ch in s:
            new_dp = (dp * 2) % MOD

            # Remove subsequences that were duplicated because
            # this character appeared before.
            if ch in last:
                new_dp = (new_dp - last[ch]) % MOD

            last[ch] = dp
            dp = new_dp

        # Exclude the empty subsequence
        return (dp - 1) % MOD
