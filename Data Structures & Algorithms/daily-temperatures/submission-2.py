class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        stack.append((temperatures[0], 0))
        for i in range(1, len(temperatures)):
            curr = temperatures[i]
            # print(stack)
            while(stack and stack[-1][0] < curr):
                output[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            stack.append((curr, i))
        return output