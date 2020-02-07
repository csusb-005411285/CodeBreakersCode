# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    # init a var to store the TreeNode
    insertedTreeNode: TreeNode
    # check if root is None
    if root is None:
      # set root to the new TreeNode
      return TreeNode(val)
    
    # if value in root equals val
    if root.val == val:
      return root
      # then duplicate is found
      # return the existing Node
      
    # if val is less than the root's val
    if val < root.val:  
      # then go to left node by recursively calling the method
      root.left = self.insertIntoBST(root.left, val)
    # else
    else:
      # then go to the right node by recursively calling the method
      root.right = self.insertIntoBST(root.right, val)
      
    # return TreeNode  
    return root
