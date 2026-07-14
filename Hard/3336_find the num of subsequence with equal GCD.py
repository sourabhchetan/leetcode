from collections import defaultdict

class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        dp = {(0, 0): 1}

        for num in nums:
            new_dp = defaultdict(int)

            for (g1, g2), cnt in dp.items():
                # Skip current number
                new_dp[(g1, g2)] = (new_dp[(g1, g2)] + cnt) % MOD

                # Add to first subsequence
                ng1 = num if g1 == 0 else self.gcd(g1, num)
                new_dp[(ng1, g2)] = (new_dp[(ng1, g2)] + cnt) % MOD

                # Add to second subsequence
                ng2 = num if g2 == 0 else self.gcd(g2, num)
                new_dp[(g1, ng2)] = (new_dp[(g1, ng2)] + cnt) % MOD

            dp = new_dp

        answer = 0

        for (g1, g2), cnt in dp.items():
            if g1 != 0 and g1 == g2:
                answer = (answer + cnt) % MOD

        return answer