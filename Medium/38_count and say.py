class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"

        for _ in range(1, n):
            res = []
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    res.append(str(count))
                    res.append(s[i - 1])
                    count = 1

            res.append(str(count))
            res.append(s[-1])

            s = "".join(res)

        return s