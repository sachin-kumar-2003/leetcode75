'''437. Path Sum III'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    ans=[0]
    hashMap={0:1}
    def dfs(node,total):
      if node is None:
        return 
      total+=node.val
      ans[0]+=hashMap.get(total-targetSum,0)
      hashMap[total]=hashMap.get(total,0)+1
      dfs(node.left,total)
      dfs(node.right,total)
      hashMap[total]-=1
    dfs(root,0)
    return ans[0]