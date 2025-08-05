'''216. Combination Sum III'''
from typing import List
class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    def recursion(idx,k,n,total,temp):
      if len(temp)==k:
        if total==n:
          ans.append(temp[:])
        return 
      if idx>9:return
      
      temp.append(idx)
      recursion(idx+1,k,n,total+idx,temp)
      temp.pop()
      recursion(idx+1,k,n,total,temp)
    ans=[]
    recursion(1,k,n,0,[])  
    return ans   