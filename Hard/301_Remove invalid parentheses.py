class Solution(object):
    def removeInvalidParentheses(self, s):
        def valid(x):
            balance = 0

            for ch in x:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = [s]
        visited = set([s])

        while queue:
            ans = []

            for cur in queue:
                if valid(cur):
                    ans.append(cur)

            if ans:
                return ans

            next_level = []

            for cur in queue:
                for i in range(len(cur)):
                    if cur[i] not in '()':
                        continue

                    if i > 0 and cur[i] == cur[i - 1]:
                        continue

                    nxt = cur[:i] + cur[i + 1:]

                    if nxt not in visited:
                        visited.add(nxt)
                        next_level.append(nxt)

            queue = next_level
