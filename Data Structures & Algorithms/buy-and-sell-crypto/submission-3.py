class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = [0] * len(prices)
        buy[0] = prices[0]
        i = 1
        while(i < len(prices)):
            buy[i] = min(prices[i], buy[i - 1])
            print(prices[i], buy[i - 1])
            i += 1

        sell = [0] * len(prices)
        sell[len(prices) - 1] = prices[len(prices) - 1]
        i = len(prices) - 2
        while(i >= 0):
            sell[i] = max(prices[i], sell[i + 1])
            i -= 1

        max_s = 0
        while(i < len(prices)):
            max_s = max(max_s, sell[i] - buy[i])
            i += 1

        return max_s

        