class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = set(nums)

        # All XOR values obtainable using two elements
        pair_xor = set()

        for a in vals:
            for b in vals:
                pair_xor.add(a ^ b)

        # All XOR values obtainable using three elements
        result = set()

        for x in pair_xor:
            for a in vals:
                result.add(x ^ a)

        return len(result)