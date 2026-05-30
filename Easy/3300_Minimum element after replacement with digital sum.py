class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_sum = float('inf')

        for num in nums:
            digit_sum = 0

            while num > 0:
                digit_sum += num % 10
                num //= 10

            min_sum = min(min_sum, digit_sum)

        return min_sum