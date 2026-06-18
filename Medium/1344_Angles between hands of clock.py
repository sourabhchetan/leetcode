class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour %= 12

        hour_angle = 30 * hour + 0.5 * minutes
        minute_angle = 6 * minutes

        diff = abs(hour_angle - minute_angle)

        return min(diff, 360 - diff)