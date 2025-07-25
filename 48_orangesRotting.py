'''994. Rotting Oranges'''
from collections import deque
from typing import List
class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    m,n=len(grid)-1,len(grid[0])-1
    freshOrange,rottenOrange=[0,0]
    q=deque()
    for i in range(m+1):
      for j in range(n+1):
        if grid[i][j]==1:freshOrange+=1
        if grid[i][j]==2:
          q.append((i,j))
          rottenOrange+=1
    if freshOrange==0:return 0
    if rottenOrange==0:return -1
    steps=0
    while q:
      steps+=1
      newQ=[]
      for  r,c in q:
        direction=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        for i,j in direction:
          if 0<=i<=m and 0<=j<=n and grid[i][j]==1:
            freshOrange-=1
            grid[i][j]=2
            if freshOrange==0:return steps
            newQ.append((i,j))
      q=newQ  
    return -1