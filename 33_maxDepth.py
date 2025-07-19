'''104. Maximum Depth of Binary Tree'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    height=0
    def findHeight(root):
      if root == None:
          return 0
      heightL=findHeight(root.left)
      heightR=findHeight(root.right)
      height=max(heightL,heightR)+1
      return height
    return findHeight(root)