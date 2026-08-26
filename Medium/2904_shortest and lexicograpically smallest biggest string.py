class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)

        left = 0
        ones = 0
        best_len = n + 1
        ans = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            # Shrink while we have at least k ones
            while ones >= k:
                if ones == k:
                    length = right - left + 1
                    curr = s[left:right + 1]

                    if length < best_len:
                        best_len = length
                        ans = curr
                    elif length == best_len and curr < ans:
                        ans = curr

                if s[left] == '1':
                    ones -= 1
                left += 1

        return ans
