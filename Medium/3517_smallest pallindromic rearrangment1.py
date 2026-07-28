class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        half = []
        middle = ""

        for i in range(26):
            ch = chr(ord('a') + i)

            half.append(ch * (count[i] // 2))

            if count[i] % 2 == 1:
                middle = ch

        left = ''.join(half)

        return left + middle + left[::-1]