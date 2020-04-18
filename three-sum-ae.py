def threeNumberSum(array, targetSum):
    # Write your code here.
	  results = [] #n
    array.sort()
    for j in range(len(array) - 2): #n
    	  i = array[j]
		    left = j + 1
		    right = len(array) - 1
        while left < right: #n
        	if array[left] + array[right] + i == targetSum:
            	results.append([i, array[left], array[right]])
				      left += 1
				      right -= 1
            elif array[left] + array[right] + i < targetSum:
              	left += 1
            else:
              	right -= 1  
    return results 
