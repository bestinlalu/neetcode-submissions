class MinStack:

    def __init__(self):
        self.s = []
        self.l = 0
        

    def push(self, val: int) -> None:
        if self.l == 0:
            self.s.append((val, val))
        else:
            self.s.append((val, min(self.s[self.l - 1][1], val)))
        self.l += 1
        

    def pop(self) -> None:
        if self.l > 0:
            self.s.pop()
            self.l -= 1
        

    def top(self) -> int:
        return self.s[-1][0]
        

    def getMin(self) -> int:
        return self.s[-1][1]
        
