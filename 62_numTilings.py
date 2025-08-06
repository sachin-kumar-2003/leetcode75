'''790. Domino and Tromino Tiling'''
class Solution:
  def numTilings(self, n: int) -> int:
    mod=10**9+7
    print(mod)
    def recursion(n,dp):
      if n==0 or n== 1:
        return 1
      if n== 2:return 2
      if n== 3:return 5
      
      if dp[n]!=-1:
        return dp[n]
      dp[n]=2*recursion(n-1,dp)% mod+recursion(n-3,dp)% mod
      return dp[n]% mod
    dp=[-1]*(n+1)
    return recursion(n,dp)