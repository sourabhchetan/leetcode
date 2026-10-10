class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)
        diff.append(0)

        n = len(nums1)

        for i in range(n):
            need = (diff[i] - diff[i + 1]) * (i + 1)

            if k >= need:
                k -= need
            else:
                level = diff[i] - k // (i + 1)
                remainder = k % (i + 1)

                return (
                    sum(x * x for x in diff[:i + 1])
                    - sum(x * x for x in diff[:i + 1])
                    + (i + 1 - remainder) * level * level
                    + remainder * (level - 1) * (level - 1)
                    + sum(x * x for x in diff[i + 1:n])
                )

        return 0
