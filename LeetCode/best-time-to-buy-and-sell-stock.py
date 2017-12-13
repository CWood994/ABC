class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if prices is None or len(prices) == 0:
            return 0
        
        bought = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < bought:
                bought = prices[i]
            else:
                profit = max(profit, prices[i] - bought)
            
        return profit