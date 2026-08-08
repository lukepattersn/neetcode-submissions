class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l = buy, r = sell
        maxP = 0 # max profit

        while r < len(prices):
            if prices[l] < prices[r]: # buy < sell, profit
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: # buy > sell, new lowest buy point
                l = r # buy = sell
            r += 1
        return maxP
