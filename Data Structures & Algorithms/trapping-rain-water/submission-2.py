class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0
        max_l = [0] * len(height)
        max_r = [0] * len(height)
        min_a = [0] * len(height)

        i = 1
        max_l[0] = height[0]
        while(i < len(height)):
            max_l[i] = max(height[i], max_l[i - 1])
            i += 1

        i = len(height) - 2
        max_r[len(height) - 1] = height[len(height) - 1]
        while(i >= 0):
            max_r[i] = max(height[i], max_r[i + 1])
            i -= 1

        i = 0
        while(i < len(height)):
            min_a[i] = min(max_r[i], max_l[i])
            i += 1

        print(min_a)
        i = 0
        while(i < len(height)):
            vol = min_a[i] - height[i]
            if vol > 0:
                total += vol
            i += 1

        return total