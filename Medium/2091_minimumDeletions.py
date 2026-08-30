class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Put min_idx on the left and max_idx on the right
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # 1. Remove both from the front
        option1 = right + 1

        # 2. Remove both from the back
        option2 = n - left

        # 3. Remove left element from front
        #    and right element from back
        option3 = (left + 1) + (n - right)

        return min(option1, option2, option3)
