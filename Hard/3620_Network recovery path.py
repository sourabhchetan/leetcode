from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        max_cost = 0

        for u, v, c in edges:
            graph[u].append((v, c))
            indegree[v] += 1
            max_cost = max(max_cost, c)

        # Topological order
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        INF = 10 ** 30

        def check(limit):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, cost in graph[u]:
                    if cost < limit:
                        continue
                    if v != n - 1 and not online[v]:
                        continue

                    if dist[v] > dist[u] + cost:
                        dist[v] = dist[u] + cost

            return dist[n - 1] <= k

        left, right = 0, max_cost
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans