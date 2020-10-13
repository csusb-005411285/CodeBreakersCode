def numbersInPi(pi, numbers):
    # init a map to store the numbers
    hash_map = {i: True for i in range(len(numbers))} #man
    # init a cache to store the min. spaces at the index
    cache = {} #man

    # call a helper method
    # pass the pi, number, initial index, and cache
    res = numbers_in_pi_helper(pi, numbers, 0, cache)
    # return the result of the helper method
    return res if res != float('inf') else -1

def numbers_in_pi_helper(pi, hash_map, index, cache):
    # if the index is found in cache:
    if index in cache:
        return cache[index]

    # if index is equal to length of nums
    if index == len(pi): # pi
        return -1

    min_spaces = float('inf')
    # loop through the list
    for i in range(index, len(pi)):
        # get the prefix
        prefix = pi[index:i + 1]
        # check if the prefix exists in the map
        if prefix in hash_map:
            # if it does
            # call the recursive function on the suffix
            min_spaces_in_suffix = numbers_in_pi_helper(pi, hash_map, i + 1, cache) 
            min_spaces = min(min_spaces, min_spaces_in_suffix + 1)
    # store the min spaces in the index of cache
    cache[index] = min_spaces
    return cache[index]
