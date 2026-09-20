class Solution(object):
    def reverseDegree(self, s):
        ans = 0

        for i in range(len(s)):
            # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            reverse_value = 26 - (ord(s[i]) - ord('a'))

            # i + 1 because position is 1-indexed
            ans += reverse_value * (i + 1)

        return ans
