def findClosestValueInBstHelper(tree, target, closest):
	# if the tree is None
	if tree is None:
		# return closest
		return closest
	# if the current value of nodde is closer than the existing closest value
	if abs(target - tree.value) < abs(target - closest):	
		# set the current value of node to closest
		closest = tree.value
	# if current node value is equal to target 
	if tree.value == target:
		# return current node value
		return closest
	# if target is less than the current value
	if target < tree.value:
		# ccall the functionrecirsively
		# pass the current node's left value, target and closest value
		closest = findClosestValueInBstHelper(tree.left, target, closest)
	# if target is greater than the current value
	else:
		# call the function  recursively
		# pass the current node'sright value
		closest = findClosestValueInBstHelper(tree.right, target, closest)
	return closest

def findClosestValueInBst(tree, target):
    # Write your code here.
    # call a function that acts as a helper
	return findClosestValueInBstHelper(tree, target, float("inf"))

