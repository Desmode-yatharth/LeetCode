
from collections import deque
from itertools import cycle, islice
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead:
            return -1

        q = deque([("0000", 0)])
        visited = {"0000"}

        while q:
            num, moves = q.popleft()

            if num == target:
                return moves

            for idx in range(4):
                digit = int(num[idx])

                # Generate the digit before and after the current digit
                neighbors = [
                    (digit - 1) % 10,
                    (digit + 1) % 10
                ]

                for new_digit in neighbors:
                    new_num = (
                        num[:idx]
                        + str(new_digit)
                        + num[idx + 1:]
                    )

                    if new_num not in dead and new_num not in visited:
                        visited.add(new_num)
                        q.append((new_num, moves + 1))

        return -1
