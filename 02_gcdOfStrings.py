'''1071. Greatest Common Divisor of Strings'''
'''For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
'''
class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    if len(str1)<len(str2):smallStr=str1
    else:smallStr=str2
    newStr=''
    ans=''
    for ch in smallStr:
      newStr+=ch
      first=(len(str1)//len(newStr))*newStr
      second=(len(str2)//len(newStr))*newStr
      if first==str1 and second == str2:
        ans=newStr
    return ans 