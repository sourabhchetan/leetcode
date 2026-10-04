class Solution(object):
    def checkValidString(self, s):
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1      # treat '*' as ')'
                high += 1     # treat '*' as '('

            # Too many ')' in every possible interpretation
            if high < 0:
                return False

            # We cannot have a negative number of unmatched '('
            low = max(low, 0)

        return low == 0
