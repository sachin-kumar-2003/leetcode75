'''374. Guess Number Higher or Lower'''
class Solution:
  def guessNumber(self, n: int) -> int:
    start,end=1,n
    while start<=end:
      mid=(start+end)//2
      ans=guess(mid)
      if ans==-1:end=mid-1
      elif ans==1:start=mid+1
      else:
        return mid
    return -1      