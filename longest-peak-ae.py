# tc: o(n2), sc: o(n)
def longestPeak(array):
    if len(array) < 3:
        return 0

    peaks = get_peaks(array)
    path_to_from_peak = get_path_from_peak(array, peaks)

    if not path_to_from_peak:
        return 0
        
    max_len = float('-inf')

    for i in path_to_from_peak:
        max_len = max(max_len, len(path_to_from_peak[i]))

    return max_len

def get_path_from_peak(array, peaks):
    path = {} 

    for i in peaks:
        forward = i + 1
        backward = i - 1
        path[i] = [array[backward], array[i], array[forward]]

        while backward >= 0 and array[backward - 1] < array[backward]:
            path[i].append(array[backward - 1]) #
            backward -= 1

        while forward < len(array) - 1 and array[forward + 1] < array[forward]:
            path[i].append(array[forward + 1])
            forward += 1

    return path        

# 2nd attempt
# tc: o(n), sc: o(n)
def longestPeak(array):
    if len(array) < 3:
        return 0

    heights = {}
    peaks = get_peaks(array)

    if len(peaks) == 0:
        return 0

    heights = populate_default_height(heights, peaks)
    heights = get_heights(heights, array)
    
    return max(heights.values())

def get_heights(heights, array):
    for index in heights.keys():
        backward = index
        forward = index
        height_for_index = 0

        while backward > 0:
            if array[backward - 1] < array[backward]:
                height_for_index += 1
                backward -= 1
            else:
                break

        heights[index] = height_for_index + 1
        height_for_index = 0

        while forward < len(array) - 1:
            if array[forward + 1] < array[forward]:
                height_for_index += 1
                forward += 1
            else:
                break

        heights[index] += height_for_index  
    
    return heights

def populate_default_height(heights, peaks):
    for peak in peaks:
        heights[peak] = 0
    
    return heights

def get_peaks(array):
    peaks = []

    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            peaks.append(i)
    
    return peaks
