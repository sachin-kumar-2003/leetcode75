'''1318. Minimum Flips to Make a OR b Equal to c'''
class Solution:
  def minFlips(self, a: int, b: int, c: int) -> int:
    num=max(a,b,c)
    ans=0
    while num:
      alb=a&1
      blb=b&1
      clb=c&1

      a=a>>1
      b=b>>1
      c=c>>1
      num=num>>1

      if alb==0 and blb==0:
        if clb==1:ans+=1
      elif alb==0 and blb==1:
        if clb==0:ans+=1
      elif alb==1 and blb==0:
        if clb==0:ans+=1
      else:
        if clb==0:ans+=2
    return ans