class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0;
        profit = 0; 
        daliyMaxProfitArray = [0, prices[1] - prices[0]]
        currentMin = prices[0] if(prices[1] > prices[0]) else prices[1]

        for i in range(2, len(prices)):
            daliyMaxProfitArray.append(prices[i] - currentMin)
            if currentMin > prices[i]: currentMin = prices[i]
        profit = max(daliyMaxProfitArray)
        return profit if(profit > 0) else 0