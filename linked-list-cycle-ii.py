# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def __init__(self):
    self.node_in_cycle = None #1
  
  def detectCycle(self, head: ListNode) -> ListNode:
    # init two pointers
    lead = head
    lag = head
    # if the linked list has a cycle
    if self.has_cycle(head):
      # get the pointer which points to Node inside of a cycle
      lag = self.node_in_cycle
      # loop until both the pointers meet
      while lead is not lag and lead and lag: #n
        # increment both the pointer
        lead = lead.next
        lag = lag.next
      
      return lead
    
    # no cycle found
    return None
  
  def has_cycle(self, head: ListNode) -> bool:
    # init two pointers
    slow = head #1
    fast = head #1
    # loop until either one of the pointers reach None
    while slow and fast and fast.next: #n
      # increment the first pointer by one
      slow = slow.next 
      # increment the second pointer by two
      fast = fast.next.next
      
      # if both the pointers point to the same Node
      if fast is slow:
        # set the node to the node_in_cycle variable
        self.node_in_cycle = fast
        return True 
        
    return False 
