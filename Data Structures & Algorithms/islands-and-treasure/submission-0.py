class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))        
        dist = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 2147483647 and (row, col) not in visited:
                        q.append((row, col))
                        visited.add((row, col))
            dist += 1

        return
