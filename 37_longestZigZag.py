'''1372. Longest ZigZag Path in a Binary Tree'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
  def longestZigZag(self, root: Optional[TreeNode]) -> int:
    self.path=0
    def dfs(node,isLeft,total):
      if node is None:
        return 
      self.path=max(self.path,total)
      if isLeft:
        dfs(node.right,False,total+1)
        dfs(node.left,True,1)
      else:
        dfs(node.left,True,total+1)
        dfs(node.right,False,1)
    dfs(root.right,False,1)
    dfs(root.left,True,1)
    return self.path      