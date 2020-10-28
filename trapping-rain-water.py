# DP
class Solution:
    def trap(self, height: [int]) -> int:
        # use two lists to store the right and left max
        boundaries = []
        # use another list to store the actual water that can be stored at the index
        water_capacity = [0 for i in range(len(height))]
        # for each index loop in forward direction
        # get the max value
        boundaries.append([0, 0])
        max_left = height[0] # 0
        for i in range(1, len(height)): # 2
            boundaries.append([max_left, 0]) # (1, 0)
            if height[i] > max_left: # 0 > 1
                max_left = height[i] # 1

        # for each index loop in backward direction
        # get the min value
        max_right = height[-1]
        for j in range(len(height) - 1, -1, -1): # 2
            boundaries[j][1] = max_right # (1, 0)
            if height[j] > max_right: # 0 > 1
                max_right = height[j] # 1
        boundaries.append([0,0])

        # loop through the heights
        for i in range(1, len(height) - 1): 
            # for each height, calculate the area.
            # get the min value from right and left.
            # subtract it from the current height
            water_capacity[i] = max(water_capacity[i], min(boundaries[i][0], boundaries[i][1]) - height[i])

        # return the sum
        return sum(water_capacity)

# One pass technique
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        # use two vars to store the max left and right values
        max_left = 0
        max_right = 0
        # use a var to store the volume
        vol = 0
        # use two pointers to loop 
        left = 0
        right = len(height) - 1
        # lopp until the two pointers cross each ohter
        while left <= right: 
            # if the left value is less than or equal to the right value
            if height[left] <= height[right]: 
                # store the max left value
                max_left = max(max_left, height[left]) 
                # calculate the cumulative volume
                if left != 0:
                    vol += max_left - height[left] 
                # increment the left pointer
                left += 1 
            # else
            else:
                # store the max right value
                max_right = max(max_right, height[right])
                # calculate the cumulative volume
                if right != len(height) - 1:
                    vol += max_right - height[right]
                # decrement the right pointer
                right -= 1
        # return the val
        return vol
