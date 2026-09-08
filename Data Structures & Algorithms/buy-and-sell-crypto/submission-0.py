class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_min_price = 100
        max_profit = 0
        profit = 0

        for x in prices:
            if last_min_price >= x:
                last_min_price = x
            if last_min_price != x:
                profit = x - last_min_price
            if profit > max_profit:
                max_profit = profit
        
        if max_profit < 0:
            return 0
        else:
            return max_profit
