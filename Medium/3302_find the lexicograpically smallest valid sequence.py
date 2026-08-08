class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n = len(word1)
        m = len(word2)

        # Positions of every character in word1
        positions = [[] for _ in range(26)]

        for i, ch in enumerate(word1):
            positions[ord(ch) - 97].append(i)

        # next_diff[i] = first position >= i whose character
        # is different from word1[i]
        next_diff = [n] * n
        for i in range(n - 2, -1, -1):
            if word1[i + 1] != word1[i]:
                next_diff[i] = i + 1
            else:
                next_diff[i] = next_diff[i + 1]

        # prev_diff[i] = last position <= i whose character
        # is different from word1[i]
        prev_diff = [-1] * n
        for i in range(1, n):
            if word1[i - 1] != word1[i]:
                prev_diff[i] = i - 1
            else:
                prev_diff[i] = prev_diff[i - 1]

        # latest0[j] = largest possible index for word2[j]
        # when the suffix word2[j:] must match exactly.
        #
        # latest1[j] = largest possible index for word2[j:]
        # when at most one mismatch is allowed.
        latest0 = [-1] * (m + 1)
        latest1 = [-1] * (m + 1)

        # Empty suffix can start after the last character.
        latest0[m] = n
        latest1[m] = n

        from bisect import bisect_left, bisect_right

        for j in range(m - 1, -1, -1):
            c = ord(word2[j]) - 97

            # Exact match
            limit = latest0[j + 1]

            if limit > 0:
                arr = positions[c]
                p = bisect_left(arr, limit) - 1

                if p >= 0:
                    latest0[j] = arr[p]

            # At most one mismatch
            limit = latest1[j + 1]

            if limit > 0:
                arr = positions[c]
                p = bisect_left(arr, limit) - 1

                best = -1

                # Matching this character
                if p >= 0:
                    best = arr[p]

                # Use the one allowed mismatch
                if latest0[j + 1] > 0:
                    x = latest0[j + 1] - 1

                    if word1[x] == word2[j]:
                        x = prev_diff[x]

                    if x > best:
                        best = x

                latest1[j] = best

        # If even the whole word cannot be formed with
        # at most one mismatch.
        if latest1[0] == -1:
            return []

        answer = []
        start = 0
        mismatch_used = False

        for j in range(m):
            target = word2[j]
            c = ord(target) - 97

            # Candidate matching the current character
            arr = positions[c]
            p = bisect_left(arr, start)

            match_idx = arr[p] if p < len(arr) else n

            # Candidate using the one allowed mismatch
            mismatch_idx = n

            if not mismatch_used and start < n:
                if word1[start] != target:
                    mismatch_idx = start
                else:
                    mismatch_idx = next_diff[start]

            # We need to check whether the remaining suffix can
            # be completed after choosing this candidate.
            best_idx = n
            best_mismatch = False

            # Try exact match candidate
            if match_idx < n:
                if j == m - 1:
                    best_idx = match_idx
                    best_mismatch = False
                else:
                    if latest1[j + 1] > match_idx:
                        best_idx = match_idx
                        best_mismatch = False

            # Try mismatch candidate
            if not mismatch_used and mismatch_idx < n:
                if j == m - 1:
                    if mismatch_idx < best_idx:
                        best_idx = mismatch_idx
                        best_mismatch = True
                else:
                    if latest0[j + 1] > mismatch_idx:
                        if mismatch_idx < best_idx:
                            best_idx = mismatch_idx
                            best_mismatch = True

            if best_idx == n:
                return []

            answer.append(best_idx)
            start = best_idx + 1

            if best_mismatch:
                mismatch_used = True

        return answer