def sameBsts(arrayOne, arrayTwo):
    return same_bsts_helper(arrayOne, arrayTwo)

def same_bsts_helper(a, b):
    # base case
    # if the lengths are 0
    if len(a) == 0 and len(b) == 0:    
        # then return true
        return True

    # if the lengths are not equal
    if len(a) != len(b):    
        # then return false
        return False

    # if the first element is not equal 
    if a[0] != b[0]: # 10 10
        # then return false
        return False
    
    # reduction step
    # get an array of elements greater than and less than the first element of both the arrays
    values_less_than_a = get_values_lesser_than(a[1:], a[0]) # 10 [15 8 12 94 81 5 2 11]
    values_greater_than_a = get_values_greater_than(a[1:], a[0])
    values_less_than_b = get_values_lesser_than(b[1:], b[0])
    values_greater_than_b = get_values_greater_than(b[1:], b[0])

    # compare the boolean values and return
    return same_bsts_helper(values_greater_than_a, values_greater_than_b) and same_bsts_helper(values_less_than_a, values_less_than_b)
    
def get_values_lesser_than(a, val):
    res = []

    for i in range(len(a)):  # 0
        if a[i] < val: # 11 <= 10
            res.append(a[i])

    return res

def get_values_greater_than(a, val):
    res = []

    for i in range(len(a)):
        if a[i] >= val:
            res.append(a[i])

    return res
