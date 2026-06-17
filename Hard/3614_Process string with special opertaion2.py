class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lengths = [0]

        for ch in s:
            cur = lengths[-1]

            if 'a' <= ch <= 'z':
                lengths.append(cur + 1)

            elif ch == '*':
                lengths.append(max(0, cur - 1))

            elif ch == '#':
                lengths.append(cur * 2)

            else:  # '%'
                lengths.append(cur)

        if k >= lengths[-1]:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            before = lengths[i]

            if 'a' <= ch <= 'z':
                if k == before:
                    return ch

            elif ch == '*':
                pass

            elif ch == '#':
                if k >= before:
                    k -= before

            else:  # '%'
                k = before - 1 - k

        return '.'