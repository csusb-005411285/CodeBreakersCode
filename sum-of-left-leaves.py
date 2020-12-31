# Post order traversal
class Solution:
    def __init__(self):
        self.sum_left_leaves = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum_of_left_leaves_helper(root)
        return self.sum_left_leaves
    
    def sum_of_left_leaves_helper(self, node):
        if not node: return
        self.sum_of_left_leaves_helper(node.left)
        self.sum_of_left_leaves_helper(node.right)
        if node.left and not node.left.left and not node.left.right: self.sum_left_leaves += node.left.val
        return

# Inorder traversal
class Solution:
     def __init__(self):
        self.total = 0
        self.isleaf = lambda node: (node is not None) and (not node.left) and (not node.right)
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum_of_left_leaves_helper(root)
        return self.total
    
    def sum_of_left_leaves_helper(self, node):
        if not node: return 0    
        if self.isleaf(node.left):
            self.total += node.left.val
        self.sum_of_left_leaves_helper(node.left)
        self.sum_of_left_leaves_helper(node.right)
        isLeaf = lambda node: (not node.left) and (not node.right) 

# Iterative in-order
class Solution:
  def sumOfLeftLeaves(self, root: TreeNode) -> int:
    if not root:
       return 0

      stack = deque()
      stack.append(root)
      total = 0
      while stack:
          node = stack.pop()
          if node.right:
              stack.append(node.right)
          if node.left:
              total += node.left.val if isLeaf(node.left) else 0
              stack.append(node.left)
      return total 
