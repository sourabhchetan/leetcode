class Solution(object):
    def resultArray(self, nums, k):
        # prev[r] = number of subarrays ending at the previous index
        # whose product % k == r
        prev = [0] * k

        # ans[r] = total number of subarrays whose product % k == r
        ans = [0] * k

        for num in nums:
            x = num % k
            curr = [0] * k

            # Start a new subarray at this element
            curr[x] += 1

            # Extend every previous subarray
            for r in range(k):
                if prev[r]:
                    new_r = (r * x) % k
                    curr[new_r] += prev[r]

            # Add all subarrays ending here
            for r in range(k):
                ans[r] += curr[r]

            prev = curr

        return ans
