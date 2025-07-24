'''450. Delete Node in a BST'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    def dfs(node,key):
      if not node:return None
      if node.val==key:
        if node.left==None and node.right == None:
          return None
        if node.left==None:
          return node.right
        if node.right==None:
          return node.left
        else:
          temp=node.right
          while temp.left:
            temp=temp.left
          node.val=temp.val
          node.right=dfs(node.right,temp.val)
      if node.val<key:
        node.right=dfs(node.right,key)
      else:
        node.left=dfs(node.left,key)
      return node

    root=dfs(root,key)
    return root