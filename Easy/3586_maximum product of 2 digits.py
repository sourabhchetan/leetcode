class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        largest = 0
        second = 0

        while n > 0:
            digit = n % 10
            n //= 10

            if digit >= largest:
                second = largest
                largest = digit
            elif digit > second:
                second = digit

        return largest * second