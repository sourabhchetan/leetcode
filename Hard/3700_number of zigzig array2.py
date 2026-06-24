class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 1000000007

        m = r - l + 1
        sz = 2 * m

        # State:
        # 0..m-1     : up[v]
        # m..2m-1    : down[v]

        T = [[0] * sz for _ in range(sz)]

        # new_up[v] = sum(down[u]) for u < v
        for v in range(m):
            for u in range(v):
                T[v][m + u] = 1

        # new_down[v] = sum(up[u]) for u > v
        for v in range(m):
            for u in range(v + 1, m):
                T[m + v][u] = 1

        # Initial state for length = 2
        state = [0] * sz

        for v in range(m):
            state[v] = v              # up[v]
            state[m + v] = m - 1 - v  # down[v]

        def mat_mul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]

            for i in range(n):
                Ai = A[i]
                Ci = C[i]

                for k in range(n):
                    if Ai[k] == 0:
                        continue

                    aik = Ai[k]
                    Bk = B[k]

                    for j in range(n):
                        if Bk[j]:
                            Ci[j] = (Ci[j] + aik * Bk[j]) % MOD

            return C

        def mat_vec_mul(A, vec):
            n = len(A)
            res = [0] * n

            for i in range(n):
                total = 0
                row = A[i]

                for j in range(n):
                    if row[j]:
                        total = (total + row[j] * vec[j]) % MOD

                res[i] = total

            return res

        power = n - 2

        while power > 0:
            if power & 1:
                state = mat_vec_mul(T, state)

            T = mat_mul(T, T)
            power >>= 1

        return sum(state) % MOD