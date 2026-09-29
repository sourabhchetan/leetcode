class Solution(object):
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Path length must be even for balance to become 0
        if (m + n - 1) % 2 == 1:
            return False

        # dp[j] = set of possible balances at column j
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if grid[i][j] == ')':
                        return False
                    dp[j].add(1)
                    continue

                balance = 1 if grid[i][j] == '(' else -1
                current = set()

                # From top
                if i > 0:
                    for b in dp[j]:
                        nb = b + balance
                        if nb >= 0:
                            current.add(nb)

                # From left
                if j > 0:
                    for b in dp[j - 1]:
                        nb = b + balance
                        if nb >= 0:
                            current.add(nb)

                dp[j] = current

        return 0 in dp[n - 1]
