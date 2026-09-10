import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        N = len(points)
        minheap = []
        par = [i for i in range(N)]
        rank = [1] * N
        adjMap = {}
        cost = 0

        i = 0
        for p, q in points:
            adjMap[i] = (p, q)
            i += 1

        for i in range(N):
            p1, q1 = adjMap[i][0], adjMap[i][1]
            for j in range(i + 1, N):
                p2, q2 = adjMap[j][0], adjMap[j][1]
                c = abs(p1 - p2) + abs(q1 - q2)
                if c == 0:
                    continue
                heapq.heappush(minheap, (c, (i, j)))

        def find(p):
            if par[p] == p:
                return p
            np = find(par[p])
            par[p] = np
            return np
        
        def union(p, q):
            par1 = find(p)
            par2 = find(q)
            if par1 == par2:
                return False
            elif rank[par1] > rank[par2]:
                par[par2] = par1
                rank[par1] += rank[par2]
            else:
                par[par1] = par2
                rank[par2] += rank[par1]
            return True

        while minheap:
            c, (p, q) = heapq.heappop(minheap)
            if union(p, q):
                cost += c

        return cost
        