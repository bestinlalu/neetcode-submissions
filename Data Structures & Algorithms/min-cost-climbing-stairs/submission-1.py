class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        l = len(cost)
        costmap = {}

        def stair(i) -> int:
            if i >= l:
                return 0
            if i in costmap:
                return costmap[i]
            costmap[i] = cost[i] + min(stair(i + 1), stair(i + 2))
            return costmap[i]

        
        return min(stair(0), stair(1))