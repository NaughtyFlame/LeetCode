class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low, high = sys.maxint, sys.maxint
        profit = 0
        for price in prices:
            if price > high:
                high = price
            else:
                profit += high - low
                low, high = price, price       
        
        return profit + high - low
        
"""
Function belong first version
"""
class Solution0(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float("Inf")
        profit = 0
        if len(prices) <= 1:
            return 0
        for index in range(len(prices) - 1):
            if prices[index] < min_price:
                min_price = prices[index]
            elif prices[index] > prices[index+1]:
                profit = profit + prices[index] - min_price
                min_price = float("Inf")
        
        if prices[len(prices)-1] > min_price:
            profit = profit + prices[len(prices)-1] - min_price
        
        return profit
