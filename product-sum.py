def productSum(array):
    return product_sum_helper(array, 1)

def product_sum_helper(a, mult):
    _sum = 0

    for i in range(len(a)):
        if type(a[i]) == list:
            _sum += product_sum_helper(a[i], mult + 1)
        else:
            _sum += a[i]
    
    return _sum * mul
