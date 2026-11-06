class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
        }
        if len(s) < 2:
            return False
        for c in s:
            
            if c in bracket_map:
                if not stack or bracket_map[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        return False
            