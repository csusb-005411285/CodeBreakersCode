def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
	# init a list to store the number of ways to make change
	# init it to 1 and have n elements
	num_ways_change = [1 for _ in range(n)]
	# loop until the n
	for amt in range(n):
		# for every n calculate the number of ways you could make the change given the
		# denominations
		for den in denoms:
			# if the number is less than the denomination 
			if amt  < den:
				# then there are 0 ways to make the change
				num_ways_change[amt] += 0
			# if the number is greater than the denomination
    		else:
				# then compute the sum from the index of that denomination and the index of the number - denomination
				num_ways_change[amt] += num_ways_change[amt] + num_ways_change[den - amt]
	# return the last index of the list
	return num_ways_change[-1]
