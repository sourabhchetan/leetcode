class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        i = 0
        n = len(words)

        while i < n:
            # Find how many words fit on this line
            j = i
            line_length = 0

            while j < n:
                needed = line_length + len(words[j]) + (j - i)

                if needed > maxWidth:
                    break

                line_length += len(words[j])
                j += 1

            num_words = j - i
            total_spaces = maxWidth - line_length

            # Last line or line containing only one word
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                gaps = num_words - 1

                spaces_each = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                parts = []

                for k in range(i, j - 1):
                    parts.append(words[k])

                    spaces = spaces_each

                    # Left gaps get extra spaces
                    if k - i < extra_spaces:
                        spaces += 1

                    parts.append(" " * spaces)

                parts.append(words[j - 1])
                line = "".join(parts)

            result.append(line)
            i = j

        return result