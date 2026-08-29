class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original_index)
        arr = sorted((nums[i], i) for i in range(n))

        ans = nums[:]
        start = 0

        for i in range(1, n + 1):
            # End of a connected component
            if i == n or arr[i][0] - arr[i - 1][0] > limit:
                group = arr[start:i]

                # Values should be assigned to the smallest indices
                # in sorted order.
                values = sorted(x[0] for x in group)
                indices = sorted(x[1] for x in group)

                for idx, val in zip(indices, values):
                    ans[idx] = val

                start = i

        return ans
