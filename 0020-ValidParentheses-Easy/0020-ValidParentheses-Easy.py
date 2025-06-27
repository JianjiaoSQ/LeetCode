class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for e in s:
            if not stack:
                stack.append(e)
                continue
            if e is ')' and stack[-1] is '(':
                stack.pop()
            elif e is ']' and stack[-1] is '[':
                stack.pop()
            elif e is '}' and stack[-1] is '{':
                stack.pop()
            else:
                stack.append(e)
        return True if not stack else False
            
        