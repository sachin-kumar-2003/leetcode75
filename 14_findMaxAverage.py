'''643. Maximum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted
Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75'''
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total=0
        for i in range(k):
           total+=nums[i]
        prevTotal=total
        for i in range(k,len(nums)):
            prevTotal=prevTotal-nums[i-k]+nums[i]
            total=max(total,prevTotal)
        return total/k