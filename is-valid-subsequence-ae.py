# tc: o(n), sc: o(n)
def isValidSubsequence(array, sequence):
    seq_indx = 0
    arr_index = 0
    subsequence = []

    while arr_index < len(array) and seq_indx < len(sequence):
        if sequence[seq_indx] == array[arr_index]:
            subsequence.append(sequence[seq_indx]) #confusing variable names
            seq_indx += 1
        arr_index += 1
        
    return len(sequence) == len(subsequence
