class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        # We need C(n + k - 1, 2k)
        N = n + k - 1

        # factorials
        fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD

        # modular inverse using Fermat's theorem
        inv_fact = [1] * (N + 1)
        inv_fact[N] = pow(fact[N], MOD - 2, MOD)

        for i in range(N, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        # C(N, 2k)
        return fact[N] * inv_fact[2 * k] % MOD * inv_fact[N - 2 * k] % MOD
