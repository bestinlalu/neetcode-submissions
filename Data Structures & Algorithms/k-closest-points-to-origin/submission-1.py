import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []

        for p in points:
            distances.append((math.pow(p[0], 2)+ math.pow(p[1],2), p))

        heapq.heapify(distances)
        res = []

        for i in range(k):
            res.append(heapq.heappop(distances)[1])
        return res
        