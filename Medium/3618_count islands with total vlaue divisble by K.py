class Solution(object):
    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                total = grid[r][c]
                grid[r][c] = 0
                stack = [(r, c)]

                while stack:
                    x, y = stack.pop()

                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy

                        if (0 <= nx < m and 0 <= ny < n
                                and grid[nx][ny] > 0):
                            total += grid[nx][ny]
                            grid[nx][ny] = 0
                            stack.append((nx, ny))

                if total % k == 0:
                    ans += 1

        return ans
