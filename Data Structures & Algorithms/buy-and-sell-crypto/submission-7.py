class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_min_price = prices[0]
        max_profit = 0
        profit = 0

        for x in prices:
            if last_min_price >= x:
                last_min_price = x
            profit = x - last_min_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit