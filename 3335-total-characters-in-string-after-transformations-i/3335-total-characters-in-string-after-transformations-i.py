class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for _ in range(t):
            # z -> ab:  every 'z' produces one 'a' and one 'b'
            cnt_z = freq[25] % MOD
            # shift: each letter i moves to i+1 (for i = 0..24)
            for i in range(25, 0, -1):
                freq[i] = freq[i - 1] % MOD
            freq[0] = cnt_z            # new 'a' from z
            freq[1] = (freq[1] + cnt_z) % MOD  # new 'b' from z (added to shifted c)
        return sum(freq) % MOD