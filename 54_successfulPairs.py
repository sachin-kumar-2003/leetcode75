'''2300. Successful Pairs of Spells and Potions'''
from typing import List
class Solution:
  def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    ans=[]
    potions.sort()
    for i in range(len(spells)):
      left,right=0,len(potions)-1
      mid=0
      while left<right:
        mid=(left+right)//2
        if spells[i]*potions[mid]>=success:
          right=mid-1
        else:
          left=mid+1
      if spells[i]*potions[left]>=success:ans.append(len(potions)-left)
      else:ans.append(len(potions)-left-1)
    return ans