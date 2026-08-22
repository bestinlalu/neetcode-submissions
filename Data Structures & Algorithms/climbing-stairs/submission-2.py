class Solution:

    def climbStairs(self, n: int) -> int:

        stairMap = {}

        def dfs(i) -> int:
            if i == n:
                return 1
            if i > n:
                return 0
            if i in stairMap:
                return stairMap[i]
            stairMap[i] = dfs(i + 1) + dfs(i + 2)
            return stairMap[i]
        
        dfs(0)
        return stairMap[0]