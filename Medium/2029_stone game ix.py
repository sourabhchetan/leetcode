class Solution(object):
    def stoneGameIX(self, stones):
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        # Stones divisible by 3 do not change the sum modulo 3.
        # They only change whose turn it is.
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        # Odd number of 0-mod-3 stones
        return abs(cnt[1] - cnt[2]) > 2