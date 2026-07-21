class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ones = s.count('1')

        # Augment with 1 at both ends
        t = '1' + s + '1'

        # Store lengths of zero blocks
        zero_blocks = []
        i = 0

        while i < len(t):
            if t[i] == '0':
                j = i
                while j < len(t) and t[j] == '0':
                    j += 1

                zero_blocks.append(j - i)
                i = j
            else:
                i += 1

        # A valid trade needs two zero blocks separated by
        # a non-empty block of ones.
        if len(zero_blocks) < 2:
            return ones

        best_gain = 0

        # Removing the 1-block between two consecutive zero blocks
        # joins those zero blocks. Turning the resulting zero block
        # into ones gives a net gain equal to their combined lengths.
        for i in range(len(zero_blocks) - 1):
            best_gain = max(
                best_gain,
                zero_blocks[i] + zero_blocks[i + 1]
            )

        return min(n, ones + best_gain)