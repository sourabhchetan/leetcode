class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True

            if r < 0 or r >= m or c < 0 or c >= n:
                return False

            if board[r][c] != word[index]:
                return False

            # Mark as visited
            temp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # Restore the cell
            board[r][c] = temp

            return found

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False