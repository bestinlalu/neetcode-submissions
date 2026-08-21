class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n <= 1:
            return True

        edgeMap = defaultdict(list)
        visited, cycle = set(),set()

        for v1, v2 in edges:
            edgeMap[v1].append(v2)
            edgeMap[v2].append(v1)
        print(edgeMap)

        def dfs(pre, cur):
            print(visited, cur)
            if cur in visited:
                return False
            if cur not in edgeMap:
                return True
            visited.add(cur)
            for v2 in edgeMap[cur]:
                if v2 != pre and not dfs(cur, v2):
                    visited.remove(cur)
                    return False
            edgeMap[cur] = []
            return True
        
        dfs(-1, 0)
        print(visited)
        return len(visited) == n

        