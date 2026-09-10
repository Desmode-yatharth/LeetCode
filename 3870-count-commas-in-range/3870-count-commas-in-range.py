class Solution:
    def countCommas(self, n: int) -> int:
        if n <= 999 : return 0
        strs = str(n)
        size = len(strs)
        commas_per_num = (size-1) // 3 

        return (n - 999 ) * commas_per_num