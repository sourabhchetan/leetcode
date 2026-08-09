class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        current = []

        def backtrack(start):
            if len(current) == k:
                result.append(current[:])
                return

            # We need (k - len(current)) numbers.
            # Stop early if there aren't enough numbers left.
            remaining = k - len(current)

            for num in range(start, n - remaining + 2):
                current.append(num)
                backtrack(num + 1)
                current.pop()

        backtrack(1)

        return result