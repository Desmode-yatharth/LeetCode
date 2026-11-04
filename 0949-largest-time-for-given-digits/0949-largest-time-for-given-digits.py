import itertools

class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        max_mins = -1

        # Use itertools to generate all unique 4-digit orderings
        for h1, h2, m1, m2 in set(itertools.permutations(arr)):
            hrs = h1 * 10 + h2
            mins = m1 * 10 + m2

            if hrs < 24 and mins < 60:
                total_mins = hrs * 60 + mins
                max_mins = max(max_mins, total_mins)

        if max_mins == -1:
            return ""

        best_hrs = max_mins // 60
        best_mins = max_mins % 60

        # Zero-pad hours and minutes to 2 digits automatically
        return f"{best_hrs:02d}:{best_mins:02d}"