class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()   
        l, r = 1, piles[-1]
        res, minrate = float('infinity'), float('infinity')

        while l <= r:
            m = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(p / m)
            if h >= total and m <= minrate:
                res = total
                minrate = m
            if total > h:
                l = m + 1
            else:
                r = m - 1

        return minrate
