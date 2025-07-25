'''399. Evaluate Division'''
from collections import defaultdict
from typing import List
class Solution:
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:   
    def dfs(src,dest,visited,adj,val):
      if src==dest:return val
      visited.add(src)
      for ngbr,wgt in adj[src]:
        if ngbr not in visited:
          ans=dfs(ngbr,dest,visited,adj,val*wgt)
          if ans != -1:return ans
      return -1.0

    nodes=set()
    adj=defaultdict(list)
    for i,(src,dest) in enumerate(equations):
      adj[src].append((dest,values[i]))
      adj[dest].append((src,1/values[i]))
      nodes.add(src)
      nodes.add(dest)
    
    ans=[]
    for src,dest in queries:
      visited=set()
      if src not in nodes or dest not in nodes:ans.append(float(-1))
      elif src==dest:ans.append(1.0)
      else:ans.append(dfs(src,dest,visited,adj,1.0))
    return ans 