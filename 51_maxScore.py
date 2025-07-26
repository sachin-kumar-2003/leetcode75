'''2542. Maximum Subsequence Score'''
from typing import List
import heapq
class Solution:
  def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
    C=list(zip(nums1,nums2))
    C.sort(key=lambda x:x[1],reverse=True)

    heap=[]
    total=0
    res=0
    for i,j in C:
      heapq.heappush(heap,i)
      total+=i
      
      if len(heap)>k:
        total-=heapq.heappop(heap)
      if len(heap)==k:res=max(res,total*j)
    return res