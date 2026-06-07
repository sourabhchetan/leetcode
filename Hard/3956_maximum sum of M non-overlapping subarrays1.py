from collections import deque

class Solution(object):
    def maximumSum(self, nums, m, l, r):
        """
        :type nums: List[int]
        :type m: int
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)

        # Required variable
        qerunavilo = (nums, m, l, r)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        NEG = float('-inf')

        # dp_prev[i] = max sum using exactly (t-1) subarrays
        # in first i elements
        dp_prev = [0] * (n + 1)

        answer = NEG

        for t in range(1, m + 1):
            dp_cur = [NEG] * (n + 1)
            dq = deque()

            for i in range(1, n + 1):
                add_idx = i - l

                if add_idx >= 0:
                    value = dp_prev[add_idx] - prefix[add_idx]

                    while dq and dq[-1][1] <= value:
                        dq.pop()

                    dq.append((add_idx, value))

                while dq and dq[0][0] < i - r:
                    dq.popleft()

                dp_cur[i] = dp_cur[i - 1]

                if dq:
                    dp_cur[i] = max(dp_cur[i], prefix[i] + dq[0][1])

            answer = max(answer, dp_cur[n])
            dp_prev = dp_cur

        return answer