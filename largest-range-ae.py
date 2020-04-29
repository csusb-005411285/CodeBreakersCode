# tc: o(n), sc: o(n)
def largestRange(array):
    if len(array) == 1:
        return array + array
        
    visited = {}
    max_len = 0
    visited = populate_visited(array, visited)
    result = []
    for i in range(len(array)):
        forward = i
        backward = i
        backward_val = array[backward]
        forward_val = array[forward]
        '''
        used a deque to add smaller elements to the start and larger elements to the end
        '''
        largest_range = deque() 

        while backward_val in visited: 
            if not visited[backward_val]:
                visited[backward_val] = True
                largest_range.appendleft(backward_val)
            backward_val -= 1
        '''
        how does continue work inside a for and a while loop?
        how does not and False work?
        '''
        while forward_val in visited:
            if not visited[forward_val]:
                visited[forward_val] = True
                largest_range.append(forward_val)
            forward_val += 1

        '''
        made a mistake when checking for max value
        a = () is a tuple
        a = set() is a set
        ''' 
        if len(largest_range) > max_len:
           max_len = len(largest_range)
           result = [] 
           '''
           when a set adds an element it always adds it to the begining
           '''
           result.append(largest_range[0])
           result.append(largest_range[-1])

    return result
