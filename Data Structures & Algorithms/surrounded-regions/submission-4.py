class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])
        edge = set()
        visited = set()

        def dfs(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS:
                if board[r][c] == 'X' or (r, c) in visited:
                    return
                visited.add((r, c))
                edge.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                    dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in edge and board[r][c] == 'O':
                    board[r][c] = 'X'