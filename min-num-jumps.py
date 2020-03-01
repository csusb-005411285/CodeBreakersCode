def minNumberOfJumps(array):
    # Write your code here.
	# if array has 0 element
	if len(array) <= 0:
		# then return 0
		return 0
		
	# if array has one element
	if array[0] == 0:
		# then return 0
		return 0
	
	# init a list to store the min no of jumps
	# init all indices to inf
	min_num_jumps = [float("inf") for _ in array]
	# the first index should have value 0
	min_num_jumps[0] = 0

	# loop through the array
	for first in range(1, len(array)):
		# loop the second pointer to the first index
		for second in range(first):
			# if the second pointer can jump to the first index or jump farther than
			# the first index
			if array[second] + second >= first:
				# then set the corresponding first index in the result array
				# it should be the min of the value of the second index + 1 jump and
				# the value of the first index
				min_num_jumps[first] = min(min_num_jumps[first], min_num_jumps[second] + 1)
					
	# return the last index
	return min_num_jumps[-1]
