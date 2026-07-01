from collections import deque

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        dist = [[-1] * n for _ in range(n)]
        q = deque()

        # Multi-source BFS from all thieves
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        def can(limit):
            if dist[0][0] < limit or dist[n - 1][n - 1] < limit:
                return False

            vis = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            vis[0][0] = True

            while q:
                x, y = q.popleft()

                if x == n - 1 and y == n - 1:
                    return True

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < n and 0 <= ny < n and
                        not vis[nx][ny] and
                        dist[nx][ny] >= limit):
                        vis[nx][ny] = True
                        q.append((nx, ny))

            return False

        left, right = 0, max(max(row) for row in dist)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans