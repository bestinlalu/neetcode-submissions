import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjMap = defaultdict(list)
        for edge in times:
            adjMap[edge[0]].append((edge[1], edge[2]))

        minheap = [(0, k)]

        visited = set()
        maxcost = 0
        
        while minheap:
            q = heapq.heappop(minheap)
            if q[1] in visited:
                    continue
            visited.add(q[1])
            maxcost = max(maxcost, q[0])
            edges = adjMap[q[1]]
            for edge in edges:
                if edge[0] not in visited:
                    heapq.heappush(minheap, (q[0] + edge[1], edge[0]))
        
        return -1 if len(visited) != n else maxcost
        