def longestIncreasingSubsequence(array):
    if len(array) <= 1:
        return array
        
    max_len = [1 for _ in range(len(array))]
    prev_indices = [None for _ in range(len(array))]
    last_max_index = 0 
    last_max_value = float('-inf')
    subseq = []

    for i in range(len(array)):
        curr_num = array[i]
        for j in range(0, i): 
            prev_num = array[j]

            if curr_num > prev_num and max_len[j] + 1 >= max_len[i]:
                max_len[i] = max_len[j] + 1
                prev_indices[i] = j

            if max_len[i] >= last_max_value:
                last_max_value = max_len[i]
                last_max_index = i 

    subseq.append(array[last_max_index])
    l = last_max_index

    while l is not None:
        indx = prev_indices[l]
        if indx is not None:
            subseq.append(array[indx])
        l = indx

    return list(reversed(subseq))
