def numberOfBinaryTreeTopologies(n, cache = {0: 1, 1: 1}):
    if n in cache:
        return cache[n]
    
	total_children = 0
	for lc in range(n):
		rc = n - 1 - lc
        nlc = numberOfBinaryTreeTopologies(lc)
        nrc = numberOfBinaryTreeTopologies(rc)
        total_children += nlc * nrc

    cache[n] = total_children 
    return cache[n] 
