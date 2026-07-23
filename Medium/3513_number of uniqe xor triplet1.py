class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n <= 2:
            return n

        power = 1

        while power <= n:
            power <<= 1

        return power