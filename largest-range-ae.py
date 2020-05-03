# tc: o(n), sc: o(n)
def largestRange(array):
    if len(array) == 1:
        return array + array
        
    hash_map = {}
    num_in_ranges = []
    max_len = float('-inf')
    results = []

    for j in array:
        hash_map[j] = False

    for i in range(len(array)):
        num_in_range = deque() 
        num_in_range.append(array[i])
        forward = array[i] + 1
        backward = array[i] - 1

        while forward in hash_map and not hash_map[forward]: 
            num_in_range.append(forward)
            hash_map[forward] = True
            forward += 1
        
        while backward in hash_map and not hash_map[backward]:
            num_in_range.appendleft(backward)
            hash_map[backward] = True
            backward -= 1
        
        num_in_ranges.append(list(num_in_range))

    for ranges in num_in_ranges:
        if len(ranges) > max_len:
            max_len = len(ranges)
            results.append(ranges[0])
            results.append(ranges[-1])
    return results
