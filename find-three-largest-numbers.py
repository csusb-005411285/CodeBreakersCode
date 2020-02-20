def findThreeLargestNumbers(array):
    # Write your code here.
    # init a list to store the three largest numbers
	three_largest_nums = [None, None, None]
	# loop through the array
	for num in array:
		# for each number check 
		# if it is greater than the last element of result list
		if three_largest_nums[2] is None or num >= three_largest_nums[2]:
			# move the 2nd element to the 1st index
			# remove the first element
			three_largest_nums[0] = three_largest_nums[1]
			# move the 3rd element to the 2nd  index
			three_largest_nums[1] = three_largest_nums[2]
			# insert the number in the 3rd index
			three_largest_nums[2] = num
		# else if the number is greater than the 2nd element of result list
		elif three_largest_nums[1] is None or num >= three_largest_nums[1]:	
			# move the 2nd element to the 1st element
			# remove the first element
			three_largest_nums[0] = three_largest_nums[1]
			# insert the number in the 2nd index
			three_largest_nums[1] = num
		# else if the number is greater than the 1st element 
		elif three_largest_nums[0] is None or num >= three_largest_nums[0]:
			# override the 1st element with the number
			three_largest_nums[0] = num
		else:
			continue
	return three_largest_nums
