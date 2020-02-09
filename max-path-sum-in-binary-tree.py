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
