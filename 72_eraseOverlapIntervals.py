'''435. Non-overlapping Intervals '''
from typing import List
class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
      intervals=sorted(intervals, key=lambda x:x[1])
      print(intervals)
      prev=0
      ans=0
      for i in range(len(intervals)):
        if i==0:continue
        if intervals[i][0]<intervals[prev][1]:
          ans+=1
        else:prev=i
      return ans