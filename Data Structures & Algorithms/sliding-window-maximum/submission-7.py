import heapq
import sys

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        A = [(-nums[i], i) for i in range(0, k)]
        heapq.heapify(A)
        # output.append(-A[0][0])
        l = 0
        for r in range(k, len(nums)):
            # print(A, l, r)
            output.append(-A[0][0])
            heapq.heappush(A, (-nums[r], r))
            l += 1
            while((A[0][0] == -nums[l - 1] and A[0][1] == l)
                    or A[0][1] < l):
                # print("popping", A[0])
                heapq.heappop(A)
        output.append(-A[0][0])
        # print(A)
        return output
