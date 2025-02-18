'''1456. Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.'''
class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    vowels=['a','e','i','o','u'] 
    start,end,ans,curr=0,k,0,0
    for i in range(k):
      if s[i] in vowels:
        ans+=1
    curr=ans
    while end<len(s):
      if s[end-k] in vowels:
        curr-=1
      if s[end] in vowels:
        curr+=1
      end+=1
      ans=max(ans,curr)
    return ans    