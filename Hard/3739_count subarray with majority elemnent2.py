class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        prefix = [0]
        cur = 0

        for x in nums:
            cur += 1 if x == target else -1
            prefix.append(cur)

        vals = sorted(set(prefix))

        rank = {}
        for i, v in enumerate(vals):
            rank[v] = i + 1

        size = len(vals)
        bit = [0] * (size + 1)

        def update(idx, delta):
            while idx <= size:
                bit[idx] += delta
                idx += idx & -idx

        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & -idx
            return s

        ans = 0

        for p in prefix:
            r = rank[p]

            # count previous prefix sums < p
            ans += query(r - 1)

            update(r, 1)

        return ans