class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = [str(i) for i in range(1, n + 1)]

        # Calculate (n - 1)!
        factorial = 1
        for i in range(1, n):
            factorial *= i

        # Convert k to 0-based index
        k -= 1

        result = []

        for remaining in range(n, 0, -1):
            index = k // factorial

            result.append(numbers.pop(index))

            k %= factorial

            if remaining > 1:
                factorial //= (remaining - 1)

        return ''.join(result)