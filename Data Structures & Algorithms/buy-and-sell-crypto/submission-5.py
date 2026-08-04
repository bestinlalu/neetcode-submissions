class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0
        buy = prices[0]
        sell = prices[1]
        max_profit = sell - buy

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i]
            else:
                sell = prices[i]
            max_profit = max(max_profit, sell - buy)

        return max_profit

            
        