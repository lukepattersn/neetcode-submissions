class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left, right = 0, 1 # buy, sell

        for p in range(len(prices) - 1 ):
            profit = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                right += 1
            maxP = max(maxP, profit)
        return maxP