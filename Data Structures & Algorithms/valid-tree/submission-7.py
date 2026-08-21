class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True

        adj = defaultdict(list)
        visited = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(pre, cur):
            if cur in visited:
                return False
            
            visited.add(cur)
            for v in adj[cur]:
                if v == pre:
                    continue
                if not dfs(cur, v):
                    return False
            return True

        return dfs(-1, 0) and n == len(visited)