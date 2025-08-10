'''452. Minimum Number of Arrows to Burst Balloons'''
from typing import List
class Solution:
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    points=sorted(points,key=lambda x:x[1])
    print(points)
    prev=0
    ans=0
    for i in range(len(points)):
      if i==0:
        ans+=1
        continue
      elif points[i][0]>points[prev][1]:
        ans+=1
        prev=i
    return ans