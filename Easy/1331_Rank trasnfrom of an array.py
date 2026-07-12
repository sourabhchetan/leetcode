class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank = {}

        for i, num in enumerate(sorted(set(arr))):
            rank[num] = i + 1

        return [rank[num] for num in arr]