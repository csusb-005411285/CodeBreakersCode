def quickselect(array, k):
    return quickselect_helper(array, 0, len(array) - 1, k - 1)

def quickselect_helper(array, start_index, end_index, position):
    while True:
        pivot = start_index
        left = pivot + 1
        right = end_index 
        while left <= right:
            pivot_val = array[pivot]
            left_val = array[left]
            right_val = array[right]
            if left_val < pivot_val:
                left += 1
            elif right_val > pivot_val:
                right -= 1
            elif left_val > pivot_val and right_val < pivot_val:
                array[left], array[right] = array[right], array[left]
        array[pivot], array[right] = array[right], array[pivot]
        if right == position:
            return array[right]
        elif position < right:
            end_index = right - 1
        else:
            start_index = right + 1
