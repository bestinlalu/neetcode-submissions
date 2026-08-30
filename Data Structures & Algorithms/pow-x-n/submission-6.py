class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        x = x if n > 0 else 1 / x
        n = abs(n)

        def calPow(x2, n2):
            if n2 == 0:
                return 1
            half = calPow(x2, n2 // 2)
            if n2 % 2 == 0:
                return half * half
            else:
                return half * half * x2
        
        return calPow(x, n)