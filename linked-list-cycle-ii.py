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
  
# 2nd attempt
class Solution:
    def __init__(self):
      self.node_in_cycle = None #1
  
    def detectCycle(self, head: ListNode) -> ListNode:
      if not head:
        return None
      
      if not head.next:
        return None
      
      # if the linked list has a cycle
      if (self.has_cycle(head)):
        # get the first node of the cycle
        # return the first node of the cycle
        return self.first_node_of_cycle(head)
      return None
    
    def has_cycle(self, head: ListNode) -> bool:
      # init two pointers
      slow = head #1
      fast = head #1
      # loop through the linkedlist
      while slow and fast and fast.next: #n
        slow = slow.next
        fast = fast.next.next
        # if two pointers meet 
        if slow is fast:
          self.node_in_cycle = slow
          return True
        
      return False
    
    def first_node_of_cycle(self, head: ListNode) -> ListNode:
      start = head
      mid = self.node_in_cycle
      # loop until two pointers meet
      while start is not mid: #n
        start = start.next
        mid = mid.next
      
      return mid

# 3rd attempt
class Solution:
  def __init__(self):
    self.vert_in_cycle = None #n
  
  def detectCycle(self, head: ListNode) -> ListNode:
    # init two pointers
    start = head 
    # detect if a linked list has a cycle
    if self.has_cycle(head): 
      # loop until they are not equal
      mid = self.vert_in_cycle 
      
      while start is not mid: 
        # increment both the pointers by 1
        start = start.next
        mid = mid.next
      # then return the first node
      return start
      
    return None
  
  def has_cycle(self, vert):
    # init two pointers
    slow = vert #1
    fast = vert #1
    # loop until they are not at the same spot
    while slow is not None and fast is not None and fast.next is not None: #n
      # loop the first pointer by 1
      slow = slow.next
      # loop the second pointer by 2
      fast = fast.next.next
      
      if slow is fast:
        self.vert_in_cycle = slow
        return True
      
    return False
