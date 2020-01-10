# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  # Write a function to reverse the linked list
  def reverse(self, head: ListNode) -> ListNode:
    prev = None
    curr = head
    while(curr is not None):
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
    return prev
  
  def isPalindrome(self, head: ListNode) -> bool:
    if (head is None):
      return True
    if (head.next is None):
      return True
    #initalize two pointers: slow and fast
    slow = head
    fast = head

    #loop fast until the end of the list
    while(fast is not None and fast.next is not None):
      # fast moves two nodes at a time
      fast = fast.next.next
      # slow moves one node at a time
      slow = slow.next


    # reverse the nodes from the point where slow ends
    slow = Solution.reverse(self, slow)
    # initialize fast to head Node
    fast = head        
    # loop until slow reaches the end. At this point slow should start from the middle
    while(slow is not None):  
      # as you traverse check if the values are not the same
      if (slow.val != fast.val):
        return False
      # slow and fast increment by one node
      slow = slow.next
      fast = fast.next
    return True
      
