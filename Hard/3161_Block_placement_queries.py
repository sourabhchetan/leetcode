from bisect import bisect_left
from sortedcontainers import SortedList

class FenwickMax:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & -idx

    def query(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res = max(res, self.bit[idx])
            idx -= idx & -idx
        return res


class Solution:
    def getResults(self, queries):
        MAXX = 50000

        # All obstacles that exist after all insertions
        obstacles = set()
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        sl = SortedList([0, MAXX])
        for x in obstacles:
            sl.add(x)

        bit = FenwickMax(MAXX + 2)

        # Initialize gaps in final state
        for i in range(1, len(sl)):
            bit.update(sl[i], sl[i] - sl[i - 1])

        ans = []

        # Process in reverse
        for q in reversed(queries):
            if q[0] == 2:
                _, x, sz = q

                idx = sl.bisect_right(x) - 1
                pre = sl[idx]

                best_gap = max(
                    bit.query(pre),
                    x - pre
                )

                ans.append(best_gap >= sz)

            else:
                _, p = q

                idx = sl.bisect_left(p)
                left = sl[idx - 1]
                right = sl[idx + 1]

                # Removing p merges intervals
                bit.update(right, right - left)

                sl.remove(p)

        return ans[::-1]