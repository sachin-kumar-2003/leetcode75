'''198. House Robber'''
from typing import List
class Solution:
  def rob(self, nums: List[int]) -> int:
    def recursion(idx,nums,dp):
      if idx>=len(nums):
        return 0
      if dp[idx]!=-1:
        return dp[idx]
      dp[idx]= max(recursion(idx+1,nums,dp),recursion(idx+2,nums,dp)+nums[idx])
      return dp[idx]
    dp=[-1]*(len(nums)+1)

    return recursion(0,nums,dp)     