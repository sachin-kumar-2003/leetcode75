'''236. Lowest Common Ancestor of a Binary Tree'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(node,arr,target):
      if not node:return None
      arr.append(node)
      if node==target:
        return list(arr)
      left=dfs(node.left,arr,target)
      if left:return left
      right=dfs(node.right,arr,target)
      if right:return right
      arr.pop()
      return None
    arr1=dfs(root,[],p)
    arr2=dfs(root,[],q)
    i=0
    while i<len(arr1) and i<len(arr2) and arr1[i]==arr2[i]:
      i+=1
    return arr2[i-1] if i>0 else None