class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods reachable from k
        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            u = stack.pop()
            for v in graph[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    stack.append(v)

        # If any non-suspicious method invokes a suspicious one,
        # nothing can be removed.
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return remaining methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans