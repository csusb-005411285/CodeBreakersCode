# tc: o(n), sc: o(1)
def subarraySort(array):
    out_of_order_elements = find_out_of_order_elements(array)
    
    if not out_of_order_elements:
        return [-1, -1]

    max_element = max(out_of_order_elements)
    min_element = min(out_of_order_elements)

    lowest_index = get_lowest_index(array, min_element)
    largest_index = get_largest_index(array, max_element)

    return [lowest_index, largest_index]

def get_largest_index(array, max_ele):
    index = len(array) - 1 
    i = len(array) - 1 

    while i >= 0:
        if max_ele > array[i]:
            return i

        i -= 1
    
    return index 

def get_lowest_index(array, min_ele):
    index = 0 
    i = 0

    while i < len(array):
        if min_ele < array[i]:
            return i

        i += 1
    
    return index

def find_out_of_order_elements(array):
    out_of_order = []

    for i in range(len(array)):
        if i == 0 and array[i] > array[i + 1]:
            out_of_order.append(array[i])
        elif i == len(array) - 1 and array[i] < array[i - 1]:
            out_of_order.append(array[i])
        elif i != 0 and i != len(array) - 1: 
            if array[i] < array[i - 1] or array[i] > array[i + 1]:
                out_of_order.append(array[i])

    return out_of_order

