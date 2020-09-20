class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        return self.trim_bst_helper(root, low, high)
    
    def trim_bst_helper(self, node, lb, ub):
        if node is None:
            return None
        
        if node.val < lb:
            return self.trim_bst_helper(node.right, lb, ub)
            
        if node.val > ub:
            return self.trim_bst_helper(node.left, lb, ub)
        
        lc = self.trim_bst_helper(node.left, lb, ub)
        rc = self.trim_bst_helper(node.right, lb, ub)

        node.left = lc
        node.right = rc

        return node   
