class Solution:
    def isValid(self, s: str) -> bool:
        openParens = "([{"
        stack = []
        
        for c in s:
            if c in openParens:
                stack.append(c)  
            elif c == ")" and stack and stack[-1] != "(":
                return False
            elif c == "]" and stack and stack[-1] != "[":
                return False
            elif c == "}" and stack and stack[-1] != "{":
                return False
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False