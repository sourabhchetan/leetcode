class Solution(object):
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])

        # prev[j] stores all possible XOR values reaching
        # column j in the previous row.
        prev = [set() for _ in range(n)]

        for i in range(m):
            curr = [set() for _ in range(n)]

            for j in range(n):
                val = grid[i][j]

                if i == 0 and j == 0:
                    curr[j].add(val)
                    continue

                # Reach from above
                if i > 0:
                    for x in prev[j]:
                        curr[j].add(x ^ val)

                # Reach from the left
                if j > 0:
                    for x in curr[j - 1]:
                        curr[j].add(x ^ val)

            prev = curr

        return min(prev[n - 1])
