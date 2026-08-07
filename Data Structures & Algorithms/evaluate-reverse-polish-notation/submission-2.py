class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        s = []
        i = 0
        while(i < len(tokens)):
            t = tokens[i]
            if t in ["+", "-", "*", "/"] and s:
                r = s.pop()
                l = s.pop()
                if t == "+":
                    s.append(l + r)
                elif t == "-":
                    s.append(l - r)
                elif t == "*":
                    s.append(l * r)
                elif t == "/":
                    s.append(int(l / r))
            else:
                s.append(int(t))
            i += 1
        return s[0]