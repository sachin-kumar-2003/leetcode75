'''1493. Longest Subarray of 1's After Deleting One Element
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.'''
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=0
        l=0
        count=0
        for r in range(len(nums)):
            if 0==nums[r]:
                count+=1
            while count>1:
                if 0==nums[l]:
                    count-=1
                l+=1
            ans=max(ans,r-l)
        return ans