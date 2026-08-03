class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights) - 1

        while (i < j):
            h = min(heights[i], heights[j])
            b = abs(i - j)
            a = b * h
            if a > area:
                area = a
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            
            

        return area
        