from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        # Find start, litter positions, and assign each litter a bit
        start = None
        litter = []

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter.append((r, c))

        k = len(litter)

        # No litter
        if k == 0:
            return 0

        litter_id = {}
        for i, (r, c) in enumerate(litter):
            litter_id[(r, c)] = i

        target = (1 << k) - 1

        # BFS:
        # (row, col, remaining_energy, collected_mask, moves)
        q = deque()
        q.append((start[0], start[1], energy, 0, 0))

        # For each (r, c, mask), keep the maximum energy seen.
        # If we reach the same state with less/equal energy,
        # it can never be better.
        best = {}

        best[(start[0], start[1], 0)] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            r, c, e, mask, moves = q.popleft()

            if mask == target:
                return moves

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                # Need 1 energy to make a move
                if e == 0:
                    continue

                ne = e - 1
                nmask = mask

                # Collect litter
                if (nr, nc) in litter_id:
                    bit = 1 << litter_id[(nr, nc)]
                    nmask |= bit

                # Reset energy on R
                if classroom[nr][nc] == 'R':
                    ne = energy

                state = (nr, nc, nmask)

                # Only keep this state if we have MORE energy
                # than any previous visit with the same position/mask.
                if state in best and best[state] >= ne:
                    continue

                best[state] = ne
                q.append((nr, nc, ne, nmask, moves + 1))

        return -1
