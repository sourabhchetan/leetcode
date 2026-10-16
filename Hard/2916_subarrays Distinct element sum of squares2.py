class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        total = [0] * (2 * size)
        squares = [0] * (2 * size)
        lazy = [0] * (2 * size)

        def apply(node, length, val):
            squares[node] = (squares[node] + 2 * val * total[node] + val * val * length) % MOD
            total[node] = (total[node] + val * length) % MOD
            lazy[node] += val

        def push(node, left, right):
            if lazy[node] != 0 and left != right:
                mid = (left + right) // 2
                apply(node * 2, mid - left + 1, lazy[node])
                apply(node * 2 + 1, right - mid, lazy[node])
                lazy[node] = 0

        def update(node, left, right, ql, qr, val):
            if ql <= left and right <= qr:
                apply(node, right - left + 1, val)
                return
            push(node, left, right)
            mid = (left + right) // 2
            if ql <= mid:
                update(node * 2, left, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr, val)
            total[node] = (total[node * 2] + total[node * 2 + 1]) % MOD
            squares[node] = (squares[node * 2] + squares[node * 2 + 1]) % MOD

        ans = 0
        last = {}

        for i, x in enumerate(nums):
            start = last.get(x, -1) + 1
            update(1, 0, n - 1, start, i, 1)
            last[x] = i
            ans = (ans + squares[1]) % MOD

        return ans
