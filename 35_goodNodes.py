'''1448. Count Good Nodes in Binary Tree'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
      def dfs(node,maxNum):
        if node ==None:
          return 0
        if node.val>=maxNum:count=1
        else:count=0
        maxNum=max(maxNum,node.val)
        count+=dfs(node.left,maxNum)
        count+=dfs(node.right,maxNum)
        return count
      return dfs(root,root.val)    