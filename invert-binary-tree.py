def invertBinaryTree(tree):
    # Write your code here.
	
	# preflight
	# if root is none:
	if tree is None:
		# then retun none
		return None
	# inti a list which would act as a queue
	queue = [tree]
	# store the first element or root in the queueue
	
	# loop through the queue
	while len(queue):
		node = queue.pop()
		# pop the first element from the queue
		if node is None:
			continue
		# swap its left and right child
		node.left, node.right = node.right, node.left
		# insert the children left into  queueu
		queue.append(node.left)
		# inseert the eright child into qwqueueu
		queue.append(node.right)
	# return root
	return tree
