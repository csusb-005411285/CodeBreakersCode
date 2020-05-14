# tc: o(n), sc: o(1)
def isMonotonic(array):
    if len(array) <= 1:
        return True

	is_non_increasing = True
    is_non_decreasing = True

    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            is_non_increasing = False
        
        if array[i - 1] > array[i]:
            is_non_decreasing = False
        
    return is_non_decreasing or is_non_increasing

# tc: o(n), sc: o(1)
def isMonotonic(array):
    direction = None
    
    for i in range(1, len(array)):
        if direction == None:
            if array[i] > array[i - 1]:
                direction = 'increasing'
                continue
            elif array[i] < array[i - 1]:
                direction = 'decreasing'
                continue
            
        if direction == 'increasing':
            if array[i - 1] > array[i]:
                return False
        
        if direction == 'decreasing':
            if array[i - 1] < array[i]:
                return False
    return True
