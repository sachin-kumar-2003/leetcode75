'''72. Edit Distance'''
class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    def recursion(word1,word2,i,j):
      if j==len(word2):
        return len(word1)-i
      if i==len(word1):
        return len(word2)-j
      if dp[i][j]!=-1:
        return dp[i][j]

      if word1[i]==word2[j]:
        return recursion(word1,word2,i+1,j+1)
      
      first=recursion(word1,word2,i,j+1)+1
      second=recursion(word1,word2,i+1,j)+1
      third=recursion(word1,word2,i+1,j+1)+1

      dp[i][j]= min(first,second,third)
      return dp[i][j]
    
    dp=[[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
    return recursion(word1,word2,0,0)