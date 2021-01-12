# Global variable
class Solution:
    def __init__(self):
        self.max_path_sum = float('-inf')
        
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return None
        self._max_path_sum(root)
        return self.max_path_sum
    
    def _max_path_sum(self, node):
        if not node:
            return float('-inf')
        if node and node.left is None and node.right is None:
            self.max_path_sum = max(self.max_path_sum, node.val)
            return node.val
        left_branch_val = self._max_path_sum(node.left)
        right_branch_val = self._max_path_sum(node.right)
        max_val_branches = max(left_branch_val, right_branch_val)
        max_path = max(node.val, node.val + max_val_branches)
        self.max_path_sum = max(self.max_path_sum, node.val + left_branch_val + right_branch_val, max_path)
        return max_path

# leetcode
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0
        max_branch_path, max_path = self.max_path_sum_helper(root)
        return max_path
    
    def max_path_sum_helper(self, node):
        if not node.left and not node.right: return (node.val, node.val)
        left_path, right_path, left_tree_max_path, right_tree_max_path = float('-inf'),float('-inf'),float('-inf'),float('-inf')
        if node.left: left_path, left_tree_max_path = self.max_path_sum_helper(node.left)
        if node.right: right_path, right_tree_max_path = self.max_path_sum_helper(node.right)
        max_node = max(left_path, right_path)
        max_path_with_parent = max(max_node + node.val, node.val)
        max_sum_tree = max(left_tree_max_path, right_tree_max_path, left_path + right_path + node.val, max_path_with_parent) # pay attention to this step
        return (max_path_with_parent, max_sum_tree)

def maxPathSum(tree):
    _, max_path_sum = maxPathSumHelper(tree)
	return max_path_sum

def maxPathSumHelper(tree):
	# Write your code here.
	# if tree is None:
	if tree is None:
		# return a tuple(0,0)
		return (0, 0)
	# store the value of the left branch
	# visit the left node
	left_branch, left_branch_path_sum = maxPathSumHelper(tree.left)
	# store the value of the right branch
	# visit the right node
	right_branch, right_branch_path_sum = maxPathSumHelper(tree.right)
	# choose the max value among left and right branch
	max_branch_val = max(left_branch, right_branch)
	# choose the max value among the value chosen in the above step added to the
	# current node or the current node by itself
	max_branch_with_or_without_node = max(tree.value, max_branch_val + tree.value)
	# choose the max among: the value chosen in the above step or the summation of
	# left branch, right branch and the node itself
	max_val_branch_or_tree = max(max_branch_with_or_without_node, left_branch + right_branch + tree.value)
	# choose the max among: the value chosen in the above step, left 
	# branch, and right branch
	max_path_sum = max(max_val_branch_or_tree, left_branch_path_sum, right_branch_path_sum)
	
	# return the max value from the above step
    return (max_branch_with_or_without_node, max_path_sum)
