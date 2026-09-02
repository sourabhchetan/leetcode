class Solution(object):
    def uniformArray(self, nums1):
        n = len(nums1)

        if n == 1:
            return True

        has_odd = False
        has_even = False

        for x in nums1:
            if x % 2 == 0:
                has_even = True
            else:
                has_odd = True

        # If all numbers have the same parity,
        # simply choose nums2[i] = nums1[i].
        if has_odd and has_even:
            # We can make every element odd:
            # odd - even = odd
            # even - odd = odd
            return True

        return True
