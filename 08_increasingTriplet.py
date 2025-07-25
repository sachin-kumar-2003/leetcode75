'''334. Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a
triple of indices (i, j, k) such that i < j < k and
nums[i] < nums[j] < nums[k]. If no such indices exists,
return false.
Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.'''
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num  
            elif num <= second:
                second = num  
            else:
                return True 
        return False