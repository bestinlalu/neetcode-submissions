import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        intervals = Counter(tasks)
        maxheap = []
        for k, v in intervals.items():
            maxheap.append(-v)
        heapq.heapify(maxheap)

        time = 0
        q = collections.deque()

        while maxheap or q:
            time += 1
            if maxheap:
                count = 1 + heapq.heappop(maxheap)
                if count:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])

        return time


        

        