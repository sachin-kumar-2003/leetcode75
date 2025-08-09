'''1268. Search Suggestions System'''
from typing import List
class Solution:
  def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()
    prefixStr=""
    ans=[]
    for ch in searchWord:
      temp=[]
      prefixStr+=ch
      for word in products:
        if word.startswith(prefixStr):
          temp.append(word)
        if len(temp)==3:
          break
      ans.append(temp[:])
    return ans