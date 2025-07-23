'''1161. Maximum Level Sum of a Binary Tree'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import deque
class Solution:
  def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    def bfs(node,level):
      q=deque()
      q.append(node)
      maxTotal=float('-inf')
      maxLevel=1
      while q:
        total=0
        for i in range(len(q)):
          currNode=q.popleft()
          total+=currNode.val
          if currNode.left:q.append(currNode.left)
          if currNode.right:q.append(currNode.right)
        if total>maxTotal:
          maxLevel=level
          maxTotal=total
        level+=1
      return maxLevel
        
    return bfs(root,1)
