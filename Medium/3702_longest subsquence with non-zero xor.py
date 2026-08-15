class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0

        for x in nums:
            xor ^= x

        if xor != 0:
            return len(nums)

        # Total XOR is 0.
        # If there is a non-zero element, remove it.
        for x in nums:
            if x != 0:
                return len(nums) - 1

        # All elements are zero.
        return 0