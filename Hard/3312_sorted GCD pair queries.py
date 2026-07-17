from bisect import bisect_left

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        MAXV = max(nums)

        freq = [0] * (MAXV + 1)
        for x in nums:
            freq[x] += 1

        # count of numbers divisible by d
        divisible = [0] * (MAXV + 1)
        for d in range(1, MAXV + 1):
            for multiple in range(d, MAXV + 1, d):
                divisible[d] += freq[multiple]

        # exact number of pairs with gcd = d
        gcd_count = [0] * (MAXV + 1)
        for d in range(MAXV, 0, -1):
            cnt = divisible[d]
            pairs = cnt * (cnt - 1) // 2

            multiple = 2 * d
            while multiple <= MAXV:
                pairs -= gcd_count[multiple]
                multiple += d

            gcd_count[d] = pairs

        # prefix counts in sorted gcdPairs
        prefix = []
        values = []
        running = 0

        for g in range(1, MAXV + 1):
            if gcd_count[g] > 0:
                running += gcd_count[g]
                prefix.append(running)
                values.append(g)

        answer = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            answer.append(values[idx])

        return answer