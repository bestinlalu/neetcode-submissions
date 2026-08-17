class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(r, c):
            visited.add((r, c))
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(0, rows) and c in range(0, cols) and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
        
        return res