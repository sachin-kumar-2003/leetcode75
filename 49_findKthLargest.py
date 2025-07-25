'''215. Kth Largest Element in an Array'''
from typing import List
import heapq
class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k,nums)[-1]