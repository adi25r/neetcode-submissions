class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            if char == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            
            elif char == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()

            elif char == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
    
        if stack:
            return False
        return True
        