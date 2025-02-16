'''1679. Max Number of K-Sum Pairs
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array
whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.
Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.'''
from typing import List
class Solution:
  def maxOperations(self, nums: List[int], k: int) -> int:
    ans=0
    hashMap={}
    for i in range(len(nums)):
      if k-nums[i] in hashMap and hashMap[k-nums[i]]>0:
        ans+=1
        hashMap[k-nums[i]]-=1
      else:
        hashMap[nums[i]]=hashMap.get(nums[i],0)+1
    return ans