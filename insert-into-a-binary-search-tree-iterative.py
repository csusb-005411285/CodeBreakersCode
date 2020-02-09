# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    result: TreeNode = root
    
    if root is None:
      return TreeNode(val)
    
    while root is not None:
      if val == root.val:
        return result
      
      if val < root.val:
        if root.left is None:
          root.left = TreeNode(val)
          return result
        else:
          root = root.left
          
      elif val > root.val:
        if root.right is None:
          root.right = TreeNode(val)
          return result
        else:
          root = root.right
      
    return None
      
      
        
