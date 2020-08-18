# Recursive
def powerset(array):
    return powerset_helper(array, None)
    
def powerset_helper(a, idx):
    if idx is None:
        idx = len(a) - 1 
    elif idx < 0:
        return [[]]
    
    ele = a[idx]
    res = powerset_helper(a, idx - 1) # n

    for i in range(len(res)): # 2n
        r = res[i]
        res.append(r + [ele])

    return res

def powerset(array):
  # Write your code here.
	subset = [[]]
	for ele in array:
		for i in range(len(subset)): #
			subset.append(subset[i] + [ele]) # 
    return subset
