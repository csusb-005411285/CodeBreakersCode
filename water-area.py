def waterArea(heights):
    if not heights:
        return 0

    max_height_left_pillar = [0 for _ in range(len(heights))]
    max_height_right_pillar = [0 for _ in range(len(heights))]
    min_height_pillars = [0 for _ in range(len(heights))]
    water_area = [0 for _ in range(len(heights))]

    left_max = 0 
    for i in range(len(heights)):
        # store the max height for the current index. compare the current index value and the max height
        # of pillar found so far
        max_height_left_pillar[i] = left_max 
        
        # if the height of current index is greater than the max height of a pillar found so far
        # update the left_max 
        if heights[i] >= left_max: 
            left_max = heights[i]  

    right_max = 0 
    for i in reversed(range(len(heights))):
        max_height_right_pillar[i] = right_max
        
        if heights[i] >= right_max:
            right_max = heights[i]
    
    for i in range(len(heights)):
        min_height_pillars[i] = min(max_height_left_pillar[i], max_height_right_pillar[i])
        # if min height > current height, calculate the diff
        # if min height < current height, the value should be 0, because no water can be stored in that index
        # if min height == current height, the value should be 0
        if min_height_pillars[i] > heights[i]:
            water_area[i] = min_height_pillars[i] - heights[i]
        else:
            water_area[i] = 0
    
    return sum(water_area)
