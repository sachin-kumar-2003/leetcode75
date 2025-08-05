'''17. Letter Combinations of a Phone Number'''
from typing import List
class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    if not digits:return []
    def recursion(ch,idx,digits,phone,ans,temp):
      if idx>=len(digits):
        ans.append(temp)
        return
      newIdx=int(digits[idx])
      for newCh in phone[newIdx]:
        recursion(ch,idx+1,digits,phone,ans,temp+newCh)

    phone=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    ans=[]
    first=phone[int(digits[0])]
    for ch in first:
      recursion(ch,1,digits,phone,ans,ch)
    return ans

