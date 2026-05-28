from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #EDGE CASE:
        if len(prices)<2:
            return 0
        #STORE MIN PRICE
        min_price=prices[0]
        #STORE MAXIMUM PROFIT
        max_profit=0
        #TRAVERSE FROM SECOND ELEMENT
        for price in prices:
            #UPDATE MINIMUM PRICE
            min_price=min(min_price,price)
            #CALCULATE CURRENT PROFIT
            profit=price-min_price
            #UPDATE MAXIMUM PROFIT
            max_profit=max(max_profit,profit)
        return max_profit
obj=Solution()
print(obj.maxProfit([7,1,5,3,6,4]))