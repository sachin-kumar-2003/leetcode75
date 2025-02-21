'''2352. Equal Row and Column Pairs
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]'''
from typing import List
from collections import defaultdict,Counter
class Solution:
  def equalPairs(self, grid: List[List[int]]) -> int:
    hashMapRow=defaultdict(tuple)
    hashMapCol=defaultdict(tuple)
    ans=0
    for i in range(len(grid)):
      hashMapRow[i]=tuple(grid[i])
    for i in range(len(grid)):
      temp=[]
      for j in range(len(grid)):
          temp.append(grid[j][i])
      hashMapCol[i]=tuple(temp)
    columns=list(hashMapCol.values())
    count=Counter(columns)
    for i in hashMapRow.values(): 
      if i in columns:
        ans+=count[i]
    return ans