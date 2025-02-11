'''1768. Merge Strings Alternately'''
'''You are given two strings word1 and word2. Merge the strings
by adding letters in alternating order, starting with word1. If a
string is longer than the other, append the additional letters
onto the end of the merged string.
Return the merged string.
Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        ans=''
        while i<len(word1) and j <len(word2):
            ans+=word1[i]+word2[j]
            i+=1
            j+=1
        if i<len(word1):
            ans+=word1[i:]
        if j<len(word2):
            ans+=word2[j:]
        return ans