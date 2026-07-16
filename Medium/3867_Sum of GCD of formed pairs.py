class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        prefixGcd = []
        current_max = 0

        for num in nums:
            current_max = max(current_max, num)
            prefixGcd.append(gcd(num, current_max))

        prefixGcd.sort()

        left = 0
        right = len(prefixGcd) - 1
        answer = 0

        while left < right:
            answer += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return answer