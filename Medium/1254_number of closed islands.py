class Solution(object):
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = 1

            while stack:
                x, y = stack.pop()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < m and 0 <= ny < n
                            and grid[nx][ny] == 0):
                        grid[nx][ny] = 1
                        stack.append((nx, ny))

        # Remove islands connected to the boundary
        for r in range(m):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][n - 1] == 0:
                dfs(r, n - 1)

        for c in range(n):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[m - 1][c] == 0:
                dfs(m - 1, c)

        # Count the remaining closed islands
        count = 0

        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r, c)

        return count
