# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
      if (head is None):
        return False
      slow = head.next
      fast = head.next
      while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        
        if (slow is fast):
          return True
      return False  
        
        
# 2nd attempt
  def hasCycle(self, head: ListNode) -> bool:
    # Init two pointers
    slow = head
    fast = head

    if head is None:
      return False
    
    # If the next element of first pointer is null and the next element of the second pointer is null
    if slow.next is None and fast.next is None:
      # Then return false
      return False
    
    while slow is not None and fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next
      while slow is fast:
        return True
    
    return False
