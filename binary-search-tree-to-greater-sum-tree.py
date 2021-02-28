class Solution:
    def __init__(self):
        self.prefix_sum = 0
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self._bst_to_gst(root)
        return root
    
    def _bst_to_gst(self, node):
        if not node:
            return
        if node and not node.left and not node.right:
            self.prefix_sum += node.val
            node.val = self.prefix_sum
            return
        self._bst_to_gst(node.right)
        self.prefix_sum += node.val
        node.val = self.prefix_sum
        self._bst_to_gst(node.left)
        return 
