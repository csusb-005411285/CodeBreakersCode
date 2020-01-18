def twoNumberSum(array, targetSum):
    # Write your code here.
	if len(array) <= 1:
		return []
	
	# initialize two pointers left and right
	left = 0
	right = len(array) - 1
	# sort the array
	array.sort()
	# loop until left < right
	while left < right:
		# if array[left] + array[right] == target
		if array[left] + array[right] == targetSum:
			return [array[left], array[right]]
		if array[left] + array[right] < targetSum:
			left += 1
		else:
			right -= 1
	return []
    
