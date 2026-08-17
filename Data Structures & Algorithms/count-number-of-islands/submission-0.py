class Solution:

    res = 0

    def numIslands(self, grid: List[List[str]]) -> int:

        def isIsland(i, j, part_of_an_island):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "0":
                return
            # print(i, j, grid[i][j])
            if not part_of_an_island:
                self.res += 1
                part_of_an_island = True
            grid[i][j] = "0"
            isIsland(i + 1, j, part_of_an_island)
            isIsland(i - 1, j, part_of_an_island)
            isIsland(i, j + 1, part_of_an_island)
            isIsland(i, j - 1, part_of_an_island)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(i, j, grid[i][j]) 
                isIsland(i, j, False)
        return self.res


        