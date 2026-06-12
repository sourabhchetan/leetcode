from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7

        n = len(edges) + 1

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = 17
        while (1 << LOG) <= n:
            LOG += 1

        depth = [0] * (n + 1)
        parent = [[0] * (n + 1) for _ in range(LOG)]

        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            node = q.popleft()

            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    depth[nei] = depth[node] + 1
                    parent[0][nei] = node
                    q.append(nei)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                parent[k][v] = parent[k - 1][parent[k - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        ans = []

        for u, v in queries:
            p = lca(u, v)

            length = depth[u] + depth[v] - 2 * depth[p]

            if length == 0:
                ans.append(0)
            else:
                ans.append(pow(2, length - 1, MOD))

        return ans