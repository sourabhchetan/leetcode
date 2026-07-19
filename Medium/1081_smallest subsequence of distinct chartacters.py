class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        seen = set()

        for i, ch in enumerate(s):
            if ch in seen:
                continue

            while stack and ch < stack[-1] and last[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)