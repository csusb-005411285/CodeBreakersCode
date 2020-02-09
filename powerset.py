def powerset(array):
  # Write your code here.
	subset = [[]]
	for ele in array:
		for i in range(len(subset)): #
			subset.append(subset[i] + [ele]) # 
    return subset
