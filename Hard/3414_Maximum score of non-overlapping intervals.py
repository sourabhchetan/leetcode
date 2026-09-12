from bisect import bisect_left

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        n = len(intervals)

        # Store: start, end, weight, original_index
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by ending position
        arr.sort(key=lambda x: x[1])

        ends = [x[1] for x in arr]

        # prev[i] = number of intervals before i that can be considered
        # For non-overlap: previous end must be < current start
        prev = []

        for i in range(n):
            l = arr[i][0]

            # First position where end >= l
            # Therefore all positions before it have end < l
            p = bisect_left(ends, l)
            prev.append(p)

        # dp[i][k] = (maximum_weight, tuple_of_original_indices)
        # using first i intervals and selecting at most k intervals
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            l, r, weight, idx = arr[i - 1]

            for k in range(5):
                # Option 1: Don't take current interval
                best = dp[i - 1][k]

                # Option 2: Take current interval
                if k > 0:
                    prev_weight, prev_indices = dp[prev[i - 1]][k - 1]

                    candidate_indices = tuple(
                        sorted(prev_indices + (idx,))
                    )

                    candidate = (
                        prev_weight + weight,
                        candidate_indices
                    )

                    # Higher weight is better.
                    # If weights are equal, lexicographically smaller indices win.
                    if (candidate[0] > best[0] or
                        (candidate[0] == best[0] and
                         candidate[1] < best[1])):
                        best = candidate

                dp[i][k] = best

        # Best answer using at most 4 intervals
        return list(dp[n][4][1])