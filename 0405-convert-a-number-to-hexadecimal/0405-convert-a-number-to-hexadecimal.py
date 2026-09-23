class Solution:
    def toHex(self, num):
        hexDigits = ['0','1','2','3','4','5','6','7',
                     '8','9','a','b','c','d','e','f']
        k = num
        if num < 0:
            k = (1 << 32) + k
        if k == 0:
            return "0"
        ans = []
        while k != 0:
            rem = k % 16
            k //= 16
            ans.append(hexDigits[rem])
        return ''.join(ans[::-1])