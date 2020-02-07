def invertBinaryTree(tree):
	# preflight
	# if tre is none
	if tree is None:
		# return none
		return None
	# sqap the left and right nodes
	tree.left, tree.right = tree.right, tree.left
	# recusively call the eft node
	invertBinaryTree(tree.left)
	# recurively call the right node
	invertBinaryTree(tree.right)
