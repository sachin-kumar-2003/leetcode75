'''1143. Longest Common Subsequence'''
class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    def recursion(i,j):
      if i>=n or j>=m:
        return 0
      if dp[i][j]!=-1:
        return dp[i][j]
      if text1[i]==text2[j]:
        return 1+recursion(i+1,j+1)
      else:
        dp[i][j]= max(recursion(i+1,j),recursion(i,j+1))
        return dp[i][j]
    n,m=len(text1),len(text2)
    dp= [ [-1 for _ in range(m+1)] for _ in range(n+1)]
    return recursion(0,0)   