from bisect import bisect_right

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        def build(starts, durations):
            rides = sorted(zip(starts, durations))
            starts = [s for s, d in rides]
            durations = [d for s, d in rides]

            n = len(rides)

            pref = [0] * n
            pref[0] = durations[0]
            for i in range(1, n):
                pref[i] = min(pref[i - 1], durations[i])

            suff = [0] * n
            suff[-1] = starts[-1] + durations[-1]
            for i in range(n - 2, -1, -1):
                suff[i] = min(
                    suff[i + 1],
                    starts[i] + durations[i]
                )

            return starts, pref, suff

        waterStarts, waterPref, waterSuff = build(
            waterStartTime, waterDuration
        )

        landStarts, landPref, landSuff = build(
            landStartTime, landDuration
        )

        ans = float('inf')

        # Land -> Water
        for s, d in zip(landStartTime, landDuration):
            x = s + d

            idx = bisect_right(waterStarts, x) - 1

            if idx >= 0:
                ans = min(ans, x + waterPref[idx])

            if idx + 1 < len(waterStarts):
                ans = min(ans, waterSuff[idx + 1])

        # Water -> Land
        for s, d in zip(waterStartTime, waterDuration):
            y = s + d

            idx = bisect_right(landStarts, y) - 1

            if idx >= 0:
                ans = min(ans, y + landPref[idx])

            if idx + 1 < len(landStarts):
                ans = min(ans, landSuff[idx + 1])

        return ans