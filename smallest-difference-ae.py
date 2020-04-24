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

# 2nd attempt
# tc: o(nlogn), sc:o(1)
def smallestDifference(arrayOne, arrayTwo):
    first = 0 #1
    sec = 0 #1
    diff = float('inf') #1
    result = [] #1
    arrayOne.sort() #nlogn
    arrayTwo.sort() #nlogn
    while first < len(arrayOne) and sec < len(arrayTwo): #n
        curr_diff = arrayOne[first] - arrayTwo[sec]
        if abs(curr_diff) <= abs(diff):
            diff = curr_diff
            result = [arrayOne[first], arrayTwo[sec]]
        if arrayOne[first] < arrayTwo[sec]:
            first += 1
        elif arrayTwo[sec] < arrayOne[first]:
            sec += 1
        else:
            return [arrayOne[first], arrayTwo[sec]]

    return result
