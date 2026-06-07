class Solution(object):
    def generateValidStrings(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[str]
        """
        lavomirex = (n, k)

        ans = []

        def dfs(i, prev_one, cost, cur):
            if cost > k:
                return

            if i == n:
                ans.append(cur)
                return

            # Add '0'
            dfs(i + 1, False, cost, cur + '0')

            # Add '1' if previous character is not '1'
            if not prev_one:
                dfs(i + 1, True, cost + i, cur + '1')

        dfs(0, False, 0, "")
        return ans