def maxSumIncreasingSubsequence(array):
    if len(array) == 1:
        return [array[0], array]

    # Write your code here.
    subseq = array[:]
    seq = [None for _ in range(len(array))]
    max_index = 0
    max_val = float('-inf') 

    for i in range(len(array)):
        curr = array[i]
        for j in range(0, i):
            prev = array[j]

            if prev < curr:
                if curr + subseq[j] >= subseq[i]:
					subseq[i] = curr + subseq[j]
                	seq[i] = j

		if subseq[i] >= max_val:
			max_val = subseq[i]
			max_index = i
    
    return [max_val, create_seq(array, seq, max_index)]
