class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)
        half = n // 2

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Check if a palindrome can be formed
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(ord('a') + i)

        if odd != n % 2:
            return ""

        # Characters used in the first half
        half_cnt = [x // 2 for x in cnt]

        target_half = target[:half]

        # -------------------------------------------------
        # Case 1:
        # Use exactly target's first half.
        # The middle/right side may make it greater.
        # -------------------------------------------------
        remaining = half_cnt[:]
        possible = True

        for ch in target_half:
            idx = ord(ch) - ord('a')

            if remaining[idx] == 0:
                possible = False
                break

            remaining[idx] -= 1

        if possible:
            left = target_half

            if n % 2:
                candidate = left + middle + left[::-1]
            else:
                candidate = left + left[::-1]

            if candidate > target:
                return candidate

        # -------------------------------------------------
        # Case 2:
        # Make the first half strictly greater than
        # target's first half.
        # -------------------------------------------------
        for pos in range(half - 1, -1, -1):

            remaining = half_cnt[:]

            # Match target's prefix before pos
            possible = True

            for i in range(pos):
                idx = ord(target_half[i]) - ord('a')

                if remaining[idx] == 0:
                    possible = False
                    break

                remaining[idx] -= 1

            if not possible:
                continue

            # Choose the smallest character greater than
            # target[pos]
            cur = ord(target_half[pos]) - ord('a')

            for c in range(cur + 1, 26):

                if remaining[c] == 0:
                    continue

                remaining[c] -= 1

                # Build the smallest possible suffix
                left = target_half[:pos]
                left += chr(ord('a') + c)

                for j in range(26):
                    if remaining[j] > 0:
                        left += chr(ord('a') + j) * remaining[j]

                # Build palindrome
                if n % 2:
                    candidate = left + middle + left[::-1]
                else:
                    candidate = left + left[::-1]

                return candidate

        return ""
