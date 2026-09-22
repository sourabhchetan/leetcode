class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Tree node:
        # [product of whole segment, counts of prefix products]
        size = 1
        while size < n:
            size *= 2

        tree_prod = [1] * (2 * size)
        tree_cnt = [[0] * k for _ in range(2 * size)]

        # Build leaves
        for i in range(n):
            p = nums[i] % k
            tree_prod[size + i] = p
            tree_cnt[size + i][p] = 1

        # Merge two nodes
        def merge(left, right):
            lp, lc = left
            rp, rc = right

            prod = (lp * rp) % k
            cnt = lc[:]

            for r in range(k):
                if rc[r]:
                    nr = (lp * r) % k
                    cnt[nr] += rc[r]

            return prod, cnt

        # Build tree
        for i in range(size - 1, 0, -1):
            p, c = merge(
                (tree_prod[i * 2], tree_cnt[i * 2]),
                (tree_prod[i * 2 + 1], tree_cnt[i * 2 + 1])
            )
            tree_prod[i] = p
            tree_cnt[i] = c

        def update(pos, value):
            idx = size + pos
            p = value % k

            tree_prod[idx] = p
            tree_cnt[idx] = [0] * k
            tree_cnt[idx][p] = 1

            idx //= 2

            while idx:
                p, c = merge(
                    (tree_prod[idx * 2], tree_cnt[idx * 2]),
                    (tree_prod[idx * 2 + 1], tree_cnt[idx * 2 + 1])
                )
                tree_prod[idx] = p
                tree_cnt[idx] = c
                idx //= 2

        def query(left, right):
            # Returns aggregate for [left, right)
            left += size
            right += size

            left_nodes = []
            right_nodes = []

            while left < right:
                if left & 1:
                    left_nodes.append(
                        (tree_prod[left], tree_cnt[left])
                    )
                    left += 1

                if right & 1:
                    right -= 1
                    right_nodes.append(
                        (tree_prod[right], tree_cnt[right])
                    )

                left //= 2
                right //= 2

            result = (1, [0] * k)

            for node in left_nodes:
                result = merge(result, node)

            for node in reversed(right_nodes):
                result = merge(result, node)

            return result

        answer = []

        for index, value, start, x in queries:
            # Update persists for future queries
            update(index, value)

            # All possible remaining arrays are:
            # nums[start:start+1], nums[start:start+2], ... nums[start:n]
            _, cnt = query(start, n)

            answer.append(cnt[x])

        return answer
