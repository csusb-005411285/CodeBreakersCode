# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    # if p and q is null
    if p is None and q is None:
      # then return true
      return True
    
    # if p is null and  q is not null
    # if q is null and p is not null
    if p is None and q is not None:  
      # return false
      return False
  
    if p is not None and q is None:
      return False
    
    # if p and q are equal
    if p.val == q.val:
      # recursively call both functions
      return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    # if they are not equal
    # return false
    return False
