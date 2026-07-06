class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        end = 0

        for start, curr_end in intervals:
            if curr_end > end:
                count += 1
                end = curr_end

        return count