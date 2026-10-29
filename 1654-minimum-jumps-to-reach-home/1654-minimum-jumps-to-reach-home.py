from collections import deque

class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        forb = set(forbidden)
        limit = max(x, max(forbidden, default=0)) + a + b   # upper bound on positions

        visit = {(0, False)}                 # state = (position, last_move_was_back)
        q = deque([(0, False, 0)])           # (position, last_move_was_back, steps)

        while q:
            pos, back, steps = q.popleft()
            if pos == x:
                return steps

            # forward: always allowed
            nxt = pos + a
            if nxt <= limit and nxt not in forb and (nxt, False) not in visit:
                visit.add((nxt, False))
                q.append((nxt, False, steps + 1))

            # backward: only if the last move was not backward
            if not back:
                prv = pos - b
                if prv >= 0 and prv not in forb and (prv, True) not in visit:
                    visit.add((prv, True))
                    q.append((prv, True, steps + 1))

        return -1