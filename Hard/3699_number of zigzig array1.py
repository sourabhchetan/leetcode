class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7

        m = r - l + 1

        # Length 2 initialization
        up = [0] * (m + 1)
        down = [0] * (m + 1)

        for v in range(1, m + 1):
            up[v] = v - 1
            down[v] = m - v

        # Build lengths 3..n
        for _ in range(3, n + 1):
            pref_down = [0] * (m + 1)
            pref_up = [0] * (m + 1)

            for v in range(1, m + 1):
                pref_down[v] = (pref_down[v - 1] + down[v]) % MOD
                pref_up[v] = (pref_up[v - 1] + up[v]) % MOD

            total_up = pref_up[m]

            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)

            for v in range(1, m + 1):
                # previous value < v, last sign must have been down
                new_up[v] = pref_down[v - 1]

                # previous value > v, last sign must have been up
                new_down[v] = (total_up - pref_up[v]) % MOD

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD