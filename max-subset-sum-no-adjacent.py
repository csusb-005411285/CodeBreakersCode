def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not array:
        return 0

    if len(array) == 1:
        return array[0]

    cache = [] 
    cache.append(array[0])
    cache.append(max(array[1], array[0]))

    for i in range(2, len(array)): 
        cache.append(max(cache[i - 1], array[i] + cache[i - 2]))

    return cache[-1] 

# 2nd attempt
def maxSubsetSumNoAdjacent(array):
  	# Write your code here.
	if len(array) == 0:
		return 0
	
	if len(array) == 1:
		return array[0]
	
	if len(array) == 2:
		return max(array[0], array[1])
	
	max_subset_sum = [0 for _ in array]

	max_subset_sum[0] = array[0]
	max_subset_sum[1] = max(array[0], array[1])
	
	for i in range(2, len(array)):
		max_subset_sum[i] = max(array[i], max(max_subset_sum[i - 1], array[i] + max_subset_sum[i - 2]))
		
	return max_subset_sum[-1]
