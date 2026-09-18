class Solution(object):
    def maxNumOfSubstrings(self, s):
        n = len(s)

        # First and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        # Find the smallest valid interval for each character
        for c in range(26):
            if last[c] == -1:
                continue

            l = first[c]
            r = last[c]
            i = l
            valid = True

            while i <= r:
                x = ord(s[i]) - ord('a')

                # This character occurs before our left boundary,
                # so this interval cannot be valid.
                if first[x] < l:
                    valid = False
                    break

                r = max(r, last[x])
                i += 1

            if valid:
                intervals.append((r, l))

        # Greedily choose intervals with the smallest ending position
        intervals.sort()

        ans = []
        prev_end = -1

        for r, l in intervals:
            if l > prev_end:
                ans.append(s[l:r + 1])
                prev_end = r

        return ans
