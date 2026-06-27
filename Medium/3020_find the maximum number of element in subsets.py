from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)

        ans = 1

        # Special handling for 1
        if 1 in cnt:
            ones = cnt[1]
            if ones % 2 == 0:
                ans = max(ans, ones - 1)
            else:
                ans = max(ans, ones)

        for x in cnt:
            if x == 1:
                continue

            length = 0
            cur = x

            while cnt[cur] >= 2:
                length += 2

                if cur * cur > 10**18:
                    break

                cur = cur * cur

            if cnt[cur] >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans