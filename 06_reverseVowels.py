'''345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".'''
class Solution:
  def isVowel(self,char):
    if(char=='a'or char=='e' or char=='i' or char=='o' or char=='u'
    or char=='A'or char=='E' or char=='I' or char=='O' or char=='U'
    ):return True
    return False
  def reverseVowels(self, s: str) -> str:
    n=len(s)
    i=0
    j=n-1
    s_arr=list(s)
    while i<j:
      if(not self.isVowel(s_arr[i])):
        i+=1
      elif(not self.isVowel(s_arr[j])):
        j-=1
      else:
        s_arr[i],s_arr[j]=s_arr[j],s_arr[i]
        i+=1
        j-=1
    return ''.join(s_arr)