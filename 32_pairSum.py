'''2130. Maximum Twin Sum of a Linked List'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    ans=0
    if head is None or not head.next:
      return 0
    slow,fast=head,head
    while fast and fast.next:
      slow=slow.next
      fast=fast.next.next
    prev,curr=None,slow
    while curr:
      nextNode=curr.next
      curr.next=prev
      prev=curr
      curr=nextNode
    last,start=prev,head
    while last:
      ans=max(ans,(last.val+start.val))
      last=last.next
      start=start.next
    return ans