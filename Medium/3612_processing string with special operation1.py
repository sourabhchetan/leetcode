class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []

        for ch in s:
            if 'a' <= ch <= 'z':
                result.append(ch)

            elif ch == '*':
                if result:
                    result.pop()

            elif ch == '#':
                result.extend(result)

            elif ch == '%':
                result.reverse()

        return ''.join(result)