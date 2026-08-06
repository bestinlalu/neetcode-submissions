class Solution:
    def isValid(self, s: str) -> bool:
        b = ""

        for c in s:
            if c in ['(', '[', '{']:
                b += c
            elif c in [')', ']', '}'] and len(b) == 0:
                return False
            elif c == ')' and b[-1] != '(':
                return False
            elif c == ']' and b[-1] != '[':
                return False
            elif c == '}' and b[-1] != '{':
                return False
            elif c == ')' and b[-1] == '(':
                b = b[:-1]
            elif c == ']' and b[-1] == '[':
                b = b[:-1]
            elif c == '}' and b[-1] == '{':
                b = b[:-1]
        return b == ""