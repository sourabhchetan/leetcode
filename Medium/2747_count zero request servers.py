class Solution(object):
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        # Keep original query indices
        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        count = {}
        ans = [0] * len(queries)

        left = 0
        right = 0
        total = len(logs)

        for q, idx in sorted_queries:
            start = q - x

            # Add logs with time <= q
            while right < total and logs[right][1] <= q:
                server = logs[right][0]
                count[server] = count.get(server, 0) + 1
                right += 1

            # Remove logs with time < q - x
            while left < right and logs[left][1] < start:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            # Servers without requests
            ans[idx] = n - len(count)

        return ans
