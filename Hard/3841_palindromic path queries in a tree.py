class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Build parent, depth, and traversal order iteratively.
        parent = [-1] * n
        depth = [0] * n
        parent[0] = 0
        order = [0]

        for u in order:
            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        # Calculate subtree sizes and heavy children.
        size_sub = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            largest = 0
            for v in adj[u]:
                if parent[v] == u:
                    size_sub[u] += size_sub[v]
                    if size_sub[v] > largest:
                        largest = size_sub[v]
                        heavy[u] = v

        # Heavy-Light Decomposition.
        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in adj[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # Iterative segment tree storing XOR masks.
        seg_size = 1
        while seg_size < n:
            seg_size *= 2

        seg = [0] * (2 * seg_size)
        chars = list(s)

        for u in range(n):
            seg[seg_size + pos[u]] = 1 << (ord(chars[u]) - ord('a'))

        for i in range(seg_size - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def update(p, value):
            p += seg_size
            seg[p] = value
            p //= 2

            while p:
                seg[p] = seg[2 * p] ^ seg[2 * p + 1]
                p //= 2

        # XOR on the half-open interval [left, right).
        def range_xor(left, right):
            left += seg_size
            right += seg_size
            result = 0

            while left < right:
                if left & 1:
                    result ^= seg[left]
                    left += 1

                if right & 1:
                    right -= 1
                    result ^= seg[right]

                left //= 2
                right //= 2

            return result

        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u] + 1)
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v] + 1)
            return result

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                chars[u] = c
                update(pos[u], 1 << (ord(c) - ord('a')))

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_xor(u, v)
                answer.append((mask & (mask - 1)) == 0)

        return answer
