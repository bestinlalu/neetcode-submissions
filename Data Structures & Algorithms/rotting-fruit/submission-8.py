class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        goodoranges, minute = 0, 0
        q = collections.deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    goodoranges += 1

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q and goodoranges > 0:
            for i in range(len(q)):
                print(q)
                r, c = q.popleft()

                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1 and grid[row][col] not in visited:
                        grid[row][col] = 2
                        q.append((row, col))
                        visited.add((row, col))
                        goodoranges -= 1
            minute += 1

        return minute if goodoranges == 0 else -1
