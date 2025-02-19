'''1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans=0
        l,r=0,0
        count=0
        while r<len(nums):
          if count <=k:
            ans+=1
            ans=max(ans,r-l+1)
        return ans
