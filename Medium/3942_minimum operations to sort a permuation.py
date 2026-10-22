class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        zero = nums.index(0)
        ans = float('inf')

        # Case 1: Values increase when moving right from 0
        increasing = True

        for i in range(n):
            if nums[(zero + i) % n] != i:
                increasing = False
                break

        if increasing:
            # Rotate directly, or reverse-rotate-reverse
            ans = min(ans, zero, n - zero + 2)

        # Case 2: Values increase when moving left from 0
        decreasing = True

        for i in range(n):
            if nums[(zero - i) % n] != i:
                decreasing = False
                break

        if decreasing:
            # Reverse then rotate, or rotate then reverse
            ans = min(ans, n - zero, zero + 2)

        return -1 if ans == float('inf') else ans
