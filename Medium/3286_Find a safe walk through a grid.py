from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])

        start = health - grid[0][0]
        if start <= 0:
            return False

        best = [[-1] * n for _ in range(m)]
        best[0][0] = start

        q = deque([(0, 0, start)])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            x, y, hp = q.popleft()

            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    nhp = hp - grid[nx][ny]

                    if nhp > 0 and nhp > best[nx][ny]:
                        best[nx][ny] = nhp
                        q.append((nx, ny, nhp))

        return False