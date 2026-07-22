from bisect import bisect_left, bisect_right

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        total_ones = s.count('1')

        # Build runs: [character, start, end]
        runs = []
        i = 0

        while i < n:
            j = i
            while j + 1 < n and s[j + 1] == s[i]:
                j += 1

            runs.append((s[i], i, j))
            i = j + 1

        # Store every 1-run that has a 0-run on both sides.
        starts = []
        ends = []
        left_zero_start = []
        right_zero_end = []
        gain = []

        for i in range(1, len(runs) - 1):
            ch, st, en = runs[i]

            if (ch == '1' and
                runs[i - 1][0] == '0' and
                runs[i + 1][0] == '0'):

                lz = runs[i - 1][1]
                rz = runs[i + 1][2]

                starts.append(st)
                ends.append(en)
                left_zero_start.append(lz)
                right_zero_end.append(rz)

                gain.append((st - lz) + (rz - en))

        m = len(gain)

        if m == 0:
            return [total_ones] * len(queries)

        # Segment tree for range maximum of full gains
        size = 1
        while size < m:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(m):
            tree[size + i] = gain[i]

        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        def range_max(left, right):
            if left > right:
                return 0

            left += size
            right += size
            best = 0

            while left <= right:
                if left % 2 == 1:
                    best = max(best, tree[left])
                    left += 1

                if right % 2 == 0:
                    best = max(best, tree[right])
                    right -= 1

                left //= 2
                right //= 2

            return best

        answer = []

        for l, r in queries:

            # The middle 1-run must have at least one zero
            # inside the query on both sides.
            first = bisect_right(starts, l)
            last = bisect_left(ends, r) - 1

            if first > last:
                answer.append(total_ones)
                continue

            best = 0

            # First possible 1-run: left zero block may be clipped by l.
            j = first
            left_len = starts[j] - max(l, left_zero_start[j])
            right_len = min(r, right_zero_end[j]) - ends[j]

            if left_len > 0 and right_len > 0:
                best = max(best, left_len + right_len)

            # Last possible 1-run: right zero block may be clipped by r.
            if last != first:
                j = last
                left_len = starts[j] - max(l, left_zero_start[j])
                right_len = min(r, right_zero_end[j]) - ends[j]

                if left_len > 0 and right_len > 0:
                    best = max(best, left_len + right_len)

            # Runs strictly between first and last have complete
            # zero blocks on both sides.
            if first + 1 <= last - 1:
                best = max(best, range_max(first + 1, last - 1))

            answer.append(total_ones + best)

        return answer