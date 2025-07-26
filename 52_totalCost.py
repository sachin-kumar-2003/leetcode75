'''2462. Total Cost to Hire K Workers'''
from heapq import heappop, heappush
from typing import List
class Solution:
  def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
    n=len(costs)
    i,j=0,n-1
    heap1,heap2=[],[]
    ans=0
    while k>0:
      while len(heap1)<candidates and i<=j:
        heappush(heap1,costs[i])
        i+=1
      while len(heap2)<candidates and j>=i:
        heappush(heap2,costs[j])
        j-=1      
      
      first,second=float('inf'),float('inf')
      if heap1:first=heap1[0]
      if heap2:second=heap2[0]
      if first<=second and heap1:
        ans+=first
        heappop(heap1)
      elif heap2:
        ans+=second
        heappop(heap2)
      k-=1
    return ans