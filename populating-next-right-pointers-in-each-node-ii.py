"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
  def connect(self, root: 'Node') -> 'Node':
    head = root # O(1)
    
    while head: # O(n)
      next_head = next_tail = Node() # 
      node = head
      while node:
        if node.left:
          next_tail.next = node.left
          next_tail = node.left
        
        if node.right:
          next_tail.next = node.right
          next_tail = node.right
          
        node = node.next
      head = next_head.next
      
    return root
