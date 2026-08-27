class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Try to match target's prefix exactly using s's characters.
        for i in range(n):
            c = ord(target[i]) - ord('a')
            if cnt[c] == 0:
                break
            cnt[c] -= 1
        else:
            # target itself is achievable as a permutation of s.
            # Find the smallest permutation strictly greater than it.
            cnt = [0] * 26
            for i in range(n - 1, -1, -1):
                c = ord(target[i]) - ord('a')
                cnt[c] += 1
                for bigger in range(c + 1, 26):
                    if cnt[bigger] > 0:
                        cnt[bigger] -= 1
                        ans = target[:i] + chr(bigger + ord('a'))
                        for x in range(26):
                            ans += chr(x + ord('a')) * cnt[x]
                        return ans
            return ""

        # target[:i] was matched exactly; target[i] isn't available anymore.
        # Try position i itself first — longest matching prefix gives the
        # smallest possible answer.
        c = ord(target[i]) - ord('a')
        for bigger in range(c + 1, 26):
            if cnt[bigger] > 0:
                cnt[bigger] -= 1
                ans = target[:i] + chr(bigger + ord('a'))
                for x in range(26):
                    ans += chr(x + ord('a')) * cnt[x]
                return ans

        # No valid character at position i — backtrack to earlier positions.
        for j in range(i - 1, -1, -1):
            c = ord(target[j]) - ord('a')
            cnt[c] += 1
            for bigger in range(c + 1, 26):
                if cnt[bigger] > 0:
                    cnt[bigger] -= 1
                    ans = target[:j] + chr(bigger + ord('a'))
                    for x in range(26):
                        ans += chr(x + ord('a')) * cnt[x]
                    return ans

        return ""
