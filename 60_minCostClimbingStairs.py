'''746. Min Cost Climbing Stairs'''
from typing import List
class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    def dp(idx):
      if idx>=len(cost):
        return 0
      if memo[idx]!=-1:
        return memo[idx]
      first=dp(idx+1)+cost[idx]
      second=dp(idx+2)+cost[idx]
      memo[idx]= min(first,second)
      return memo[idx]
    memo=[-1]*(len(cost)+1)
    return min(dp(0),dp(1))  