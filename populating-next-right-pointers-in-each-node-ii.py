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

  # 5th attempt
  def connect(self, root: 'Node') -> 'Node':
    if not root:
      return None
    
    if not root.left and not root.right:
      return root
    
    slow = root
    while slow: #n
      fast = slow
      head = tail = Node('0') #1
      while fast: #n
        if fast.left:
          tail.next = fast.left
          tail = tail.next 
        if fast.right:
          tail.next = fast.right
          tail = tail.next 
        fast = fast.next
      slow = head.next
    
    return root
  
  # 6th attempt
  def connect(self, root: 'Node') -> 'Node':
    if not root:
      return None
    
    if not root.left and not root.right:
      return root
    
    # init two pointers, one would emulate dfs whereas the other would emulate bfs
    top_down = root #1
    right_left = root #1
    # init two pointers. One would store the next node for the DFS, whereas the other would connect the nodes
    head = None #1
    tail = None #1
    # outer loop; dfs
    while top_down: #n  
      # set two pointers to the node pointed by the outer loop pointer
      head = tail = Node(0)
      right_left = top_down
      # inner loop; bfs
      while right_left: #n
        # if the node has a left child
        if right_left.left:
          # also set the next pointer of third pointer to the left child
          tail.next = right_left.left
          # set the fourth pointer to the left child
          tail = tail.next
        # if the node has a right child
        if right_left.right: 
          # then the third pointer would connect this to the left child
          tail.next = right_left.right
          # the third pointer would be at the right child
          tail = tail.next 
        # the second pointer would point to the next node of the left sibling, similar to BFS operation
        right_left = right_left.next
      # the first pointer would point to the third pointer, similar to DFS operation 
      top_down = head.next
    
    return root
