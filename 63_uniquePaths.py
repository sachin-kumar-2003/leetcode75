'''62. Unique Paths'''
class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    def backtrack(row,col):
      if row>m or col>n or row<1 or col <1:
        return 0
      if row==m  and col==n:
        return 1
      if dp[row][col]!=-1:
        return dp[row][col]
      dp[row][col]= backtrack(row+1,col)+backtrack(row,col+1)
      return dp[row][col]

    dp=[[-1 for _ in range(n+1)] for _ in range(m+1)]
    return backtrack(1,1)      