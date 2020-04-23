
def threeNumberSum(array, targetSum):
    triplets = [] #n
    array.sort() # nlogn
    for i in range(len(array) - 2): #n
        result = three_number_sum_helper(array, targetSum, i)
        if result:
            triplets.extend(result)
    
    if len(triplets) == 0:
        return []

    return triplets

def three_number_sum_helper(array, target, curr):
    start = curr + 1
    end = len(array) - 1
    result = []
    while start < end: #n
        if array[curr] + array[start] + array[end] == target:
            result.append([array[curr], array[start], array[end]])
            start += 1
            end -= 1
        elif array[curr] + array[start] + array[end] > target:
            end -= 1
        else:
            start += 1
    return result 
