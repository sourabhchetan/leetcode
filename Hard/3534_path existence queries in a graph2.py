class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        order = sorted(range(n), key=lambda x: nums[x])
        values = [nums[i] for i in order]

        pos = [0] * n
        for i, node in enumerate(order):
            pos[node] = i

        # Connected components in sorted order
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        # Farthest sorted index reachable in one edge
        nxt = [0] * n
        r = 0
        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            nxt[l] = r

        LOG = 17
        while (1 << LOG) <= n:
            LOG += 1

        up = [[0] * n for _ in range(LOG)]
        up[0] = nxt[:]

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            a = pos[u]
            b = pos[v]

            if a > b:
                a, b = b, a

            # Different connected components
            if comp[a] != comp[b]:
                ans.append(-1)
                continue

            steps = 0
            cur = a

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < b:
                    cur = up[k][cur]
                    steps += 1 << k

            ans.append(steps + 1)

        return ans