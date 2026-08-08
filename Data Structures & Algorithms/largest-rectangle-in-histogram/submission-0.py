import sys

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_a = 0
        s = []
        heights.append(0)

        for i in range(0, len(heights)):
            index = i
            while(s and heights[i] < s[-1][1]):
                h = s.pop()
                max_a = max(max_a, h[1] * (i - h[0]))
                index = h[0]
            s.append((index, heights[i]))
        
        return max_a