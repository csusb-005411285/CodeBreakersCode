def maxSubsetSumNoAdjacent(array):
  	# Write your code here.
	if len(array) == 0:
		return 0
	
	if len(array) == 1:
		return array[0]
	
	if len(array) == 2:
		return max(array[0], array[1])
	# init a list to store the results
	max_subset_sum = [0 for _ in range(len(array))]
	# the first two elements of the lsit would be the same as the ones in the array
	max_subset_sum[0] = array[0]
	max_subset_sum[1] = max(array[0], array[1])
	# loop through the array 
	# start from the third element	
	for i in range(2, len(array)):
		# compute the max value for the current index
		# compare the previous index and the sum of value from current index and the
		# value from the 2 indexes before
		max_subset_sum[i] = max(max_subset_sum[i - 1], max_subset_sum[i - 2] + array[i])
	
	# return the last index of the result list
	return max_subset_sum[-1]
