class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific, common = set(), set(), []
        
        def dfs(r, c, visited, previousHeight):
            if 0 <= r < ROWS and 0 <= c < COLS and heights[r][c] >= previousHeight and (r, c) not in visited:
                visited.add((r, c))
                dfs(r + 1, c, visited, heights[r][c])
                dfs(r - 1, c, visited, heights[r][c])
                dfs(r, c + 1, visited, heights[r][c])
                dfs(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        for (r, c) in pacific:
            if (r, c) in atlantic:
                common.append([r, c])

        return common

