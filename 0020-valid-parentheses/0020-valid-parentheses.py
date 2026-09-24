class Solution:
    def isValid(self, s) :
        mapping = {')': '(', '}': '{', ']': '['}
        stk = []

        for char in s:
            if char in mapping.values():
                stk.append(char)
                continue
            elif stk and mapping[char] == stk[-1]: stk.pop()
            elif (not stk and char in mapping) or (stk and stk[-1]!= mapping[char]):       return False
        
        return len(stk) == 0