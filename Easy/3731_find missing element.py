class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        mn = min(nums)
        mx = max(nums)

        ans = []

        for num in range(mn, mx + 1):
            if num not in s:
                ans.append(num)

        return ans