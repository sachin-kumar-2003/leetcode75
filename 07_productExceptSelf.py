'''238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]'''
from typing import List
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    prefix=[]
    temp=1
    for i in range(0,len(nums),1):
      prefix.append(temp)
      temp*=nums[i]
    temp=1
    multi=[]
    for i in range(len(nums)-1,-1,-1):
      multi.insert(0,temp)
      temp*=nums[i]
    for i in range(len(nums)):
      nums[i]=prefix[i]*multi[i]
    return nums