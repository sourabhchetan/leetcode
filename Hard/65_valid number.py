class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen_digit = False
        seen_dot = False
        seen_exp = False
        digit_after_exp = True

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                seen_digit = True
                digit_after_exp = True

            elif ch == '+' or ch == '-':
                # Sign is allowed only at the beginning
                # or immediately after e/E
                if i > 0 and s[i - 1] not in 'eE':
                    return False

            elif ch == '.':
                # Dot cannot occur twice or after exponent
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            elif ch == 'e' or ch == 'E':
                # Exponent requires a number before it
                if seen_exp or not seen_digit:
                    return False

                seen_exp = True
                digit_after_exp = False

            else:
                return False

        return seen_digit and digit_after_exp