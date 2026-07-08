from bisect import bisect_left, bisect_right

class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        k = len(digits)

        pref_sum = [0] * (k + 1)
        pref_num = [0] * (k + 1)
        pow10 = [1] * (k + 1)

        for i in range(k):
            pref_sum[i + 1] = pref_sum[i] + digits[i]
            pref_num[i + 1] = (pref_num[i] * 10 + digits[i]) % MOD
            pow10[i + 1] = (pow10[i] * 10) % MOD

        answer = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r)

            if left == right:
                answer.append(0)
                continue

            length = right - left

            x = (pref_num[right] -
                 pref_num[left] * pow10[length]) % MOD

            digit_sum = pref_sum[right] - pref_sum[left]

            answer.append((x * digit_sum) % MOD)

        return answer