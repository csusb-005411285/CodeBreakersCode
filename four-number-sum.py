def fourNumberSum(array, targetSum):
    quads = [] #n 
    two_sum = {} #n

    for mid in range(1, len(array)): #n
        for forward in range(mid + 1, len(array)): #n
            diff = targetSum - (array[mid] + array[forward])
            if diff in two_sum:
                for pair in two_sum[diff]:
                    quads.append(pair + [array[mid], array[forward]])

        for backward in range(0, mid): #n
            sum_back = array[mid] + array[backward]
            if sum_back not in two_sum:
                two_sum[sum_back] = [[array[backward], array[mid]]]
            else:
                two_sum[sum_back].append([array[backward], array[mid]]) 

    return quads
