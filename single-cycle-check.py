def hasSingleCycle(array):
    # Write your code here.
	if len(array) < 0:
		return False
	# init a var to store the number of elements visited
	num_elements = 0
	# init a var to store the current index
	curr_index = 0
	next_index = 0
	# loop through the list
	while num_elements < len(array): # O(n)
		# if number of elements visited is less than thee end of the list
		# and still the current index is 0 it means we have a cycle 
		# before reaching the last element
		if num_elements > 0 and curr_index == 0:
			return False
		# increment the number of elements visited
		num_elements += 1
		# calculate the next index
		curr_index = get_next_index(curr_index, array)
	# return true if the current index is at 0
	return curr_index

def get_next_index(curr_index, array):
	next_index = 0
	# calculate the value of the current index
	value = array[curr_index]
	# next index would be the sum of current index and the value in  the 
	# current idendex
	# if the value is greater than the len of the array
	# then compute the modfrom the length of the arrya
	# and add it
	next_index = (value + curr_index) + (value+curr_index)%len(array)
	# if the current index is positive
	if next_index > 0:
		# then return the result
		return next_index
	# else
	else:
		return len(array) + next_index 
		# return the value from above plus the length of the array
	pass
