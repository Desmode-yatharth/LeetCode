class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # pop until '(' and reverse that segment
                segment = []
                while stack and stack[-1] != '(':
                    segment.append(stack.pop())
                if stack:                 # pop the '('
                    stack.pop()
                stack.extend(segment)     # push the reversed segment back
            else:
                stack.append(char)
        
        return ''.join(stack)