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

# tc: o(n2), sc: o(n2)
def fourNumberSum(array, targetSum):
    quads = []
    hashmap = {}
    forward = 0
    backward = 0
    for i in range(1, len(array) - 1):
        forward = i + 1
        backward = 0 
        while forward < len(array):
            diff = targetSum - (array[i] + array[forward])
            if diff in hashmap:
                for pair in hashmap[diff]:
                    quads.append(pair + [array[i], array[forward]])
            forward += 1

        while backward <  i:
            sum_num = array[backward] + array[i]
            if sum_num not in hashmap:
                hashmap[sum_num] = [[array[backward], array[i]]] 
            else:
                hashmap[sum_num].append([array[backward], array[i]]) 
            backward += 1
    return quads
