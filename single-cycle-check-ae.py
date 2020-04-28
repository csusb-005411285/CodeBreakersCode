# tc: o(n), sc: o(1)
def hasSingleCycle(array):
    slow = 0
    fast = 0
    num_elements_visited = 0

    while slow < len(array):
        next_index = fast + array[fast]
        if next_index == 0 and num_elements_visited >= 1 and num_elements_visited != len(array) - 1:
            return False
        if next_index < 0:
            if -next_index >= len(array):
                remainder = -next_index % len(array)
                if remainder == 0:
                    next_index = 0
                else:
                    next_index = len(array) - remainder
            else:
                next_index = len(array) + next_index
        else:
            if next_index >= len(array):
                next_index = next_index % len(array)
        num_elements_visited += 1
        fast = next_index
        slow += 1
    return num_elements_visited == len(array) and fast == 0

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

		
			
		
