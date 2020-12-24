# Concise
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_bst_helper(root, float('-inf'), float('inf'))
    
    def is_valid_bst_helper(self, node, lower_bound, upper_bound):
        if not node: return True
        if node.val <= lower_bound or node.val >= upper_bound: return False
        return self.is_valid_bst_helper(node.left, lower_bound, node.val) and self.is_valid_bst_helper(node.right, node.val, upper_bound) 
    
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
    
        if not root.left and not root.right:
            return True

        return self.is_binary_search_tree_helper(root, float('inf'), float('-inf'))

    # 50, t 30, t 10, t
    def is_binary_search_tree_helper(self, node, ub, lb): 
        if not node:
            return True
        # if the current node is greater than the upper bound or if it is less than the lower bound
        if node.val >= ub or node.val <= lb:
            return False

        # move left, set the upper bound to the current node and the lower bound to -inf
        left_child = self.is_binary_search_tree_helper(node.left, node.val, lb) 

        # move right, set the upper bound to inf and the lower bound to current node
        right_child = self.is_binary_search_tree_helper(node.right, ub, node.val)
        # return the results of the left and right child
        return left_child and right_child
