class Solution:
    def isHappy(self, n: int) -> bool:

        repeatedNos = set()
        while True:
            p = n
            if p in repeatedNos:
                return False
            if p == 1:
                return True
            repeatedNos.add(p)
            n = 0
            while p > 0:
                d = p % 10
                n = n + (d * d)
                p = p // 10
