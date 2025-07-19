'''872. Leaf-Similar Trees'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    first=[]
    second=[]
    def dfs(node,arr):
      if node==None:
        return 
      if node.left is None and node.right is None:
        arr.append(node.val)
        return 
      dfs(node.left,arr)
      dfs(node.right,arr)
    dfs(root1,first)
    dfs(root2,second)
    return first==second