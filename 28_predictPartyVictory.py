'''649. Dota2 Senate'''
from collections import deque
class Solution:
  def predictPartyVictory(self, senate: str) -> str:
    rCount,dCount=0,0
    for ch in senate:
      if ch=='R':
        rCount+=1
      else:
        dCount+=1
    senate=list(senate)
    i=0
    while rCount>0 and dCount>0:
      if senate[i]=='':
        i=(i+1)%len(senate)
        continue
      if rCount==0:return 'Dire'
      if dCount==0:return 'Radiant'
      j=(i+1)%len(senate)
      curr=senate[i]
      while rCount or dCount:
        if senate[j]!=curr and senate[j]!='':
          senate[j]=''
          if curr=='R':dCount-=1
          else:rCount-=1
          break
        j=(j+1)%len(senate)
      i=(i+1)%len(senate)
    return 'Radiant' if rCount else 'Dire'