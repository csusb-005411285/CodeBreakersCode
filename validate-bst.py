# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBstHelper(tree, min_val, max_val):
	is_left_tree_valid = False
	is_right_tree_valid = False
	# if tree is None
	if tree is None:
		# return true
		return True
	# if the value of node is less than the min value
	if tree.value < min_val:
		# return false
		return False
	# if the value of the node is greater than the max value
	if tree.value >= max_val:
		# return false
		return False
	# traverse the left side of the tree
	# pass the left node as the argument
	# pass the value of current node as max value
	is_left_tree_valid = validateBstHelper(tree.left, min_val, tree.value)
	
	# pass the right node as the argument
	# pass the max value from the argument as min value
	is_right_tree_valid = validateBstHelper(tree.right, tree.value, max_val)
	return is_left_tree_valid and is_right_tree_valid

def validateBst(tree):
    # Write your code here.
	# call the helper function with the current treee, min value as
	# negative infinity and max value as positive infinity
	return validateBstHelper(tree, float("-inf"), float("inf"))
    
