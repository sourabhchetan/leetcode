class Solution(object):
    def largestInteger(self, nums, k):
        count = {}
        n = len(nums)

        for i in range(n - k + 1):
            # Set avoids counting the same number twice
            # within the same subarray.
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for x in seen:
                count[x] = count.get(x, 0) + 1

        ans = -1

        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans