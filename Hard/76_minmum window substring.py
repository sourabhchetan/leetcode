class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        required = len(need)
        formed = 0

        left = 0
        best_len = float('inf')
        best_left = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # This character now satisfies its required frequency
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # Try to shrink the window
            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1

                left += 1

        if best_len == float('inf'):
            return ""

        return s[best_left:best_left + best_len]