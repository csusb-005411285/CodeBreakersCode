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
        
        
