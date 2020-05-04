def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort() #nlogn
    arrayTwo.sort() #mlogm
    one_ptr = 0 #1
    two_ptr = 0 #1
    min_sum = float('inf')
    result = []

    while one_ptr < len(arrayOne) and two_ptr < len(arrayTwo): #n + m
        curr_sum = float('inf') #1
        one_val = arrayOne[one_ptr]
        two_val = arrayTwo[two_ptr]
        if one_val < two_val:
            curr_sum = arrayTwo[two_ptr] - arrayOne[one_ptr]
            one_ptr += 1
        elif two_val < one_val:
            curr_sum = arrayOne[one_ptr] - arrayTwo[two_ptr]
            two_ptr += 1
        else:
            return [arrayOne[one_ptr], arrayTwo[two_ptr]]
          
        if min_sum > curr_sum:
            min_sum = curr_sum
            result = [one_val, two_val]
    return result

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    min_diff = float('inf')
    diff = 0
    one = 0
    two = 0
    while one < len(arrayOne) and two < len(arrayTwo):
        if arrayOne[one] < arrayTwo[two]:
            diff = abs(arrayTwo[two] - arrayOne[one])
            if diff <= min_diff:
                results = []
                results.append(arrayOne[one])
                results.append(arrayTwo[two])
                min_diff = diff 
            one += 1
        elif arrayTwo[two] < arrayOne[one]:
            diff = abs(arrayOne[one] - arrayTwo[two])
            if diff <= min_diff:
                results = []
                results.append(arrayOne[one])
                results.append(arrayTwo[two])
                min_diff = diff 
            two += 1
        else:
            return [arrayOne[one], arrayTwo[two]]
    return results
