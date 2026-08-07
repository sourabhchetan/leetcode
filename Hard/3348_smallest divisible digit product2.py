class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        n = len(num)

        # ---- factor t into 2^A 3^B 5^C 7^D ----
        A = B = C = D = 0
        tt = t
        while tt % 2 == 0:
            tt //= 2
            A += 1
        while tt % 3 == 0:
            tt //= 3
            B += 1
        while tt % 5 == 0:
            tt //= 5
            C += 1
        while tt % 7 == 0:
            tt //= 7
            D += 1
        if tt != 1:
            return "-1"

        DEXP = [None,
                (0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0), (2, 0, 0, 0), (0, 0, 1, 0),
                (1, 1, 0, 0), (0, 0, 0, 1), (3, 0, 0, 0), (0, 2, 0, 0)]

        dimB, dimC, dimD = B + 1, C + 1, D + 1

        def idx(x, y, z, w):
            return ((x * dimB + y) * dimC + z) * dimD + w

        size = (A + 1) * dimB * dimC * dimD
        dp = [0] * size

        for x in range(A + 1):
            for y in range(B + 1):
                for z in range(C + 1):
                    for w in range(D + 1):
                        if x == 0 and y == 0 and z == 0 and w == 0:
                            continue
                        best = None
                        for dgt in range(1, 10):
                            e2, e3, e5, e7 = DEXP[dgt]
                            nx = x - e2 if x > e2 else 0
                            ny = y - e3 if y > e3 else 0
                            nz = z - e5 if z > e5 else 0
                            nw = w - e7 if w > e7 else 0
                            if nx == x and ny == y and nz == z and nw == w:
                                continue
                            v = dp[idx(nx, ny, nz, nw)] + 1
                            if best is None or v < best:
                                best = v
                        dp[idx(x, y, z, w)] = best

        def dpv(x, y, z, w):
            return dp[idx(x, y, z, w)]

        def clamp(px, py, pz, pw):
            rx = A - px if A > px else 0
            ry = B - py if B > py else 0
            rz = C - pz if C > pz else 0
            rw = D - pw if D > pw else 0
            return rx, ry, rz, rw

        def build_min(L):
            # smallest zero-free number of exactly length L meeting full requirement
            state = (A, B, C, D)
            res = []
            for pos in range(L):
                rem_after = L - 1 - pos
                for dgt in range(1, 10):
                    e2, e3, e5, e7 = DEXP[dgt]
                    nx = state[0] - e2 if state[0] > e2 else 0
                    ny = state[1] - e3 if state[1] > e3 else 0
                    nz = state[2] - e5 if state[2] > e5 else 0
                    nw = state[3] - e7 if state[3] > e7 else 0
                    if dpv(nx, ny, nz, nw) <= rem_after:
                        res.append(str(dgt))
                        state = (nx, ny, nz, nw)
                        break
            return ''.join(res)

        # prefix exponent sums, and first zero position
        pre = [(0, 0, 0, 0)] * (n + 1)
        z_idx = n
        for i, ch in enumerate(num):
            d = int(ch)
            if d == 0:
                e = (0, 0, 0, 0)
                if z_idx == n:
                    z_idx = i
            else:
                e = DEXP[d]
            p = pre[i]
            pre[i + 1] = (p[0] + e[0], p[1] + e[1], p[2] + e[2], p[3] + e[3])

        if z_idx == n:
            rx, ry, rz, rw = clamp(*pre[n])
            if rx == 0 and ry == 0 and rz == 0 and rw == 0:
                return num

        start_i = min(z_idx, n - 1)
        for i in range(start_i, -1, -1):
            px, py, pz, pw = pre[i]
            L = n - 1 - i
            if i == z_idx:
                rng = range(1, 10)
            else:
                rng = range(int(num[i]) + 1, 10)

            found = None
            for dgt in rng:
                e2, e3, e5, e7 = DEXP[dgt]
                rx, ry, rz, rw = clamp(px + e2, py + e3, pz + e5, pw + e7)
                if dpv(rx, ry, rz, rw) <= L:
                    found = (dgt, rx, ry, rz, rw)
                    break
            if found is None:
                continue

            dgt, rx, ry, rz, rw = found
            res = list(num[:i]) + [str(dgt)]
            state = (rx, ry, rz, rw)
            for pos in range(i + 1, n):
                rem_after = n - 1 - pos
                for e in range(1, 10):
                    e2, e3, e5, e7 = DEXP[e]
                    nx = state[0] - e2 if state[0] > e2 else 0
                    ny = state[1] - e3 if state[1] > e3 else 0
                    nz = state[2] - e5 if state[2] > e5 else 0
                    nw = state[3] - e7 if state[3] > e7 else 0
                    if dpv(nx, ny, nz, nw) <= rem_after:
                        res.append(str(e))
                        state = (nx, ny, nz, nw)
                        break
            return ''.join(res)

        # No same-length completion exists (either impossible within n digits,
        # or num's suffix blocks any increment) -> answer must use more digits.
        m = dpv(A, B, C, D)
        L = max(n + 1, m)
        return build_min(L)