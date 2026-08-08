class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # mem = O(n)
        closeToOpen = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c in closeToOpen: # key is a closing parethesis, value is opening
                if stack and stack[-1] == closeToOpen[c]: # ensure stack isn't empty, stack[-1] = val we just added
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False