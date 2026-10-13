class Solution(object):
    def maxAlternatingSum(self, nums):
        nums.sort(key=lambda x: abs(x * x))
        squares = [x * x for x in nums]
        n = len(nums)
        half = (n + 1) // 2

        return sum(squares[n - half:]) - sum(squares[:n - half])
