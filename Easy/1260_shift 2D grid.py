class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total = m * n

        k %= total

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                old_pos = i * n + j
                new_pos = (old_pos + k) % total

                new_i = new_pos // n
                new_j = new_pos % n

                result[new_i][new_j] = grid[i][j]

        return result