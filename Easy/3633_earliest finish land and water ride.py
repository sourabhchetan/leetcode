class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):
        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                # Land -> Water
                land_end = landStartTime[i] + landDuration[i]
                water_start = max(land_end, waterStartTime[j])
                ans = min(ans, water_start + waterDuration[j])

                # Water -> Land
                water_end = waterStartTime[j] + waterDuration[j]
                land_start = max(water_end, landStartTime[i])
                ans = min(ans, land_start + landDuration[i])

        return ans