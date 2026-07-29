class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        LIMIT = k

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        middle = ""
        half = [0] * 26
        half_len = 0

        for i in range(26):
            half[i] = cnt[i] // 2
            half_len += half[i]

            if cnt[i] % 2:
                middle = chr(ord('a') + i)

        # Count distinct permutations, capped at LIMIT.
        def count_permutations(counts, total):
            res = 1
            remaining = total

            for c in counts:
                if c == 0:
                    continue

                # C(remaining, c), capped
                comb = 1
                for j in range(1, c + 1):
                    comb = comb * (remaining - c + j) // j

                    if comb >= LIMIT:
                        comb = LIMIT
                        break

                res *= comb

                if res >= LIMIT:
                    return LIMIT

                remaining -= c

            return res

        # Check whether k-th permutation exists
        if count_permutations(half, half_len) < k:
            return ""

        left = []

        # Construct k-th lexicographic permutation
        for pos in range(half_len):

            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1

                ways = count_permutations(
                    half,
                    half_len - pos - 1
                )

                if k > ways:
                    k -= ways
                    half[c] += 1
                else:
                    left.append(chr(ord('a') + c))
                    break

        left = ''.join(left)

        return left + middle + left[::-1]