class Solution(object):
    def minOperations(self, nums, x, k):
        n = len(nums)

        # Coordinate compression
        values = sorted(set(nums))
        rank = {v: i for i, v in enumerate(values)}
        m = len(values)

        # Fenwick trees for frequency and sum
        bit_cnt = [0] * (m + 1)
        bit_sum = [0] * (m + 1)

        def add(bit, i, delta):
            i += 1
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        # Find the index of the kth smallest element
        def kth(kth_value):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step

                if nxt <= m and bit_cnt[nxt] < kth_value:
                    idx = nxt
                    kth_value -= bit_cnt[nxt]

                step >>= 1

            return idx

        # Insert the first window
        window_sum = 0

        for i in range(x):
            v = nums[i]
            add(bit_cnt, rank[v], 1)
            add(bit_sum, rank[v], v)
            window_sum += v

        # Calculate cost of every window
        costs = []

        for start in range(n - x + 1):
            median_idx = kth((x + 1) // 2)
            median = values[median_idx]

            left_count = query(bit_cnt, median_idx + 1)
            left_sum = query(bit_sum, median_idx + 1)

            right_count = x - left_count
            right_sum = window_sum - left_sum

            cost = (
                median * left_count - left_sum +
                right_sum - median * right_count
            )

            costs.append(cost)

            # Slide the window
            if start < n - x:
                old = nums[start]
                new = nums[start + x]

                add(bit_cnt, rank[old], -1)
                add(bit_sum, rank[old], -old)

                add(bit_cnt, rank[new], 1)
                add(bit_sum, rank[new], new)

                window_sum += new - old

        # DP: minimum cost to select j non-overlapping windows
        INF = 10**30
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip the current position
                curr[i] = curr[i - 1]

                # Select window ending at i - 1
                if i >= x:
                    candidate = prev[i - x] + costs[i - x]
                    curr[i] = min(curr[i], candidate)

            prev = curr

        return prev[n]