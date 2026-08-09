import sys
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 0
        min_h = (sys.maxsize, r)
        print(l, r)

        while(l <= r):
            # mid = math.ceil((l + r) / 2)
            mid = (l + r) // 2
            hours = 0
            # print(mid, l, r)
            if mid == 0:
                break
            for i in piles:
                print(math.ceil(i / mid))
                hours += math.ceil(i / mid)
            if (hours <= h):
                # if (hours <= min_h[0]):
                min_h = (hours, mid)
                r = mid - 1
            else:
                l = mid + 1
            print(mid, l, r, min_h)
        return min_h[1]
