'''328. Odd Even Linked List'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or not head.next:
      return head 
    odd=head
    even=odd.next
    evenStart=even
    while even and even.next:
      odd.next=even.next
      odd=odd.next
      even.next=odd.next
      even=odd.next
    odd.next=evenStart
    return head