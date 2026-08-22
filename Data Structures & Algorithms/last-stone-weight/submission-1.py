class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if not stones:
            return 0

        i = len(stones) - 1

        while i >= 1:
            stones.sort()
            stones[i - 1] = abs(stones[i] - stones[i - 1])
            i -= 1

        return stones[0]
        