class Solution(object):
    def minInsertions(self, s):
        insertions = 0
        balance = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                balance += 2
                if balance % 2 == 1:
                    insertions += 1
                    balance -= 1
            else:
                balance -= 1

                if balance < 0:
                    insertions += 1
                    balance = 1

            i += 1

        return insertions + balance
