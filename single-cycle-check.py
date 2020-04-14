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

# 2nd attempt
def hasSingleCycle(array):
    # Write your code here.
	# init two pointers
	fast = 0
	slow = 0
	# init a set to store the indices
	visited = set() # O(n)
	
	# loop through the list
	while slow < len(array): # O(n)
		# calculate the index
		next_index = array[fast] + fast
		# if the value does not exist in the set
		if fast not in visited:
			if array[fast] >= 0:
				if next_index >= len(array):
					next_index = next_index % len(array)
			else:
				if next_index < 0:	
					# if sum of value and index is greater than length of list
					if -next_index >= len(array):
						# then calculate mod
						next_index = (next_index % len(array))
					else:
						next_index = next_index + len(array)
			visited.add(fast)			
		else:
			return False
		# move the fast pointer by that value
		fast = next_index		
		# increment the slow pointer
		slow += 1
	
	# compare the length of visited with the length of input array
	return len(visited) == len(array) and fast == 0

# 3rd attempt
def hasSingleCycle(array):
	if len(array) == 0:
		return False
		
	if len(array) == 1:
		return True

	start = 0 #1
	end = 0 #1
	# init a binary list
	visited = [] #n
	
	while start < len(array): #n
		next_index = array[end] + end
		if next_index >= len(array):
			remainder = next_index % len(array)
			next_index = remainder
		else:
			if next_index < 0:
				if -next_index < len(array):
					next_index = len(array) + next_index
				if -next_index >= len(array):
					remainder = -next_index % len(array)
					if remainder != 0:
						next_index = len(array) - remainder
					else:
					 	next_index = 0
					
		if end in visited:
			return False
		
		visited.append(end)
		end = next_index
		start += 1
		
	return end == 0 and len(visited) == len(array)

		
			
		
