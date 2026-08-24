class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = { k : [] for k in range(n)}
        visit = set()
        count = 0
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node):
            if node in visit:
                return False
            visit.add(node)
            for n in adj[node]:
                dfs(n)
            return True

        for n1 in adj.keys():
            if dfs(n1):
                count += 1
            if len(visit) == n:
                return count
        return -1
        