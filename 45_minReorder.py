"1466. Reorder Routes to Make All Paths Lead to the City Zero"
from typing import List
from collections import defaultdict
class Solution:
  def minReorder(self, n: int, connections: List[List[int]]) -> int:
    def dfs(curr,visited,adj,connected):
      visited.add(curr)
      for ngbr in adj[curr]:
        if ngbr not in visited:
          connected.add((ngbr,curr))
          dfs(ngbr,visited,adj,connected)
    
    connected=set()
    adj=defaultdict(list)
    visited=set()
    for src,dest in connections:   
      adj[src].append(dest) 
      adj[dest].append(src)
      connected.add((src,dest))
    
    firstLen=len(connected)
    for i in range(n):
      if i not in visited:
        dfs(i,visited,adj,connected)
    return len(connected)-firstLen