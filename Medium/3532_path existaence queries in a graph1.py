class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        comp = [0] * n
        component_id = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                component_id += 1
            comp[i] = component_id

        answer = []

        for u, v in queries:
            answer.append(comp[u] == comp[v])

        return answer