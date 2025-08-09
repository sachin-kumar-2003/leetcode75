'''338. Counting Bits'''
from typing import List
class Solution:
  def countBits(self, n: int) -> List[int]:
    ans=[]
    for i in range(n+1):
      num=i
      ones=0
      while num:
        if (num)&1:
          ones+=1
        num=num>>1
      ans.append(ones)
    return ans      