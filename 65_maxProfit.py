'''714. Best Time to Buy and Sell Stock with Transaction Fee'''
from typing import List
class Solution:
  def maxProfit(self, prices: List[int],fee: int) -> int:
    def recursion(price,idx,buy):
      if idx>=len(prices):
        return 0
      profit=0

      if dp[idx][buy]!=-1:
        return dp[idx][buy]

      if buy:
        take=recursion(price,idx+1,False)-prices[idx]
        notTake=recursion(price,idx+1,True)
        profit=max(profit,take,notTake)
      else:
        sell=prices[idx]+recursion(prices,idx+1,True)-fee
        notSell=recursion(price,idx+1,False)
        profit=max(profit,sell,notSell)
      dp[idx][buy]= profit
      return profit
    
    dp=[[-1 for _ in range(2)] for _ in range(len(prices))]
    return recursion(prices,0,True)    