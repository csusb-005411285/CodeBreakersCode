def numberOfWaysToMakeChange(n, denoms):
    # Write your code.
	if n == 0:
		return 1
		
	if len(denoms) == 0:
		return 0
		
	# init a list to store the num of ways to make change
	# include n in the list
	num_ways_change = [0 for _ in range(n + 1)]
	
	# init the 0th index to 1
	# there is 1 way to make change for 0 amount
	num_ways_change[0] = 1
	# loop through the denoms
	for deno in denoms:
		# loop through the amount till n
		for amt in range(1, n + 1):
			# if deno > amt
			if deno > amt:	
				continue

			# the no of ways is sum of value from current index and the 
			# difference between the amount and deno
			num_ways_change[amt] = num_ways_change[amt] + num_ways_change[amt - deno]			
		# return the last index 
	return num_ways_change[-1]
