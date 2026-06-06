class Solution:
    def leftRightDifference(self, nums):
        total = sum(nums)
        left_sum = 0
        answer = []

        for num in nums:
            right_sum = total - left_sum - num
            answer.append(abs(left_sum - right_sum))
            left_sum += num

        return answer