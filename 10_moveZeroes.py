'''283. Move Zeroes
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]'''
from typing import List
class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    idx=0
    for i in range(len(nums)):
      if nums[i]!=0:
        nums[idx],nums[i]=nums[i],nums[idx]
        idx+=1
        