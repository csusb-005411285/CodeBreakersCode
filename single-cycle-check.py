def hasSingleCycle(array):
    # Write your code here.
	# Since the problem is about finding a cycle, it is most likely a DFS solution
	# we need to check if all the indexes are visited and 
	# we return back to the starting index
	
	# init a var to count the number of elements visited
	num_ele_visited = 0
	# init a var to store the last position
	last_pos = 0
	# loop through the array
	# loop until the number of jumps is equal to the number of elements
	# in the array
	while num_ele_visited < len(array):
		# what if there is a cycle before we reach the last element
		if num_ele_visited > 0 and last_pos == 0:
			# return false
			return False
		# calculate the next jump
		last_pos = next_pos(array, last_pos)
		num_ele_visited += 1
	# return if last position is at 0
	return last_pos == 0
	
# define a method to calculate the next position
def next_pos(array, index):
	# Three conditions exists:
		# next jump is less than the last index of the array	
		# next jump is greater than the last index of the array
		# next jump is negative
	# init a var to store the next position
	# next pos is equal to current index + value in that index
	next_pos = (index + array[index]) % len(array)
	if next_pos >= 0:
		return next_pos
	else:
		return next_pos + len(array)


	
	
