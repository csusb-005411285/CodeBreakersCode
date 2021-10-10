class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # init vars
        cache = [0] * len(cuboids)
        max_height = 0
        sorted_cuboids = []
        # inital checks
        
        # process
        # sort each cuboid in asc. order
        for i, cube in enumerate(cuboids):
            sorted_cuboids.append(sorted(cube)) # 1. 
        # sort the complete cuboids in desc. order. Sort by width.
        sorted_cuboids.sort(key=lambda x: (-x[0], -x[1], -x[2])) # 2.
        cache[0] = sorted_cuboids[0][2]
        max_height = sorted_cuboids[0][2]
        # outer loop
        for i in range(1, len(sorted_cuboids)):
            cache[i] = sorted_cuboids[i][2]
            # inner loop, ends at the outer loop
            for j in range(i):
                if self.can_place_cuboid_on_top(sorted_cuboids[j], sorted_cuboids[i]): # 3.
                    # compare the height of the current cuboid with the height of current cuboid added to the
                    # stack of cuboids formed by the previous cubes. We use the height of cuboids as height 
                    # will have the max. value. The height is the last element of inner lists and as we are
                    # sorting it in asc. order, height will have the max. value.
                    cache[i] = max(cache[i], cache[j] + sorted_cuboids[i][2])
            # store the max value in a global variable
            max_height = max(max_height, cache[i])
        # return
        return max_height

    def can_place_cuboid_on_top(self, a, b):
        return a[0] >= b[0] and a[1] >= b[1] and a[2] >= b[2] 

'''
1. As we want to have the stack with the max. height and the height is the last element of each cube. Therefore by sorting each cube in ascending order, we are guranteed to have the largest value of each cube as the height. 
2. We sort it by descending order of width, length and height because we want the cube with the largest width, length, and height to be at the bottom.
3. The question mentions that for a cube to stack over other cube, the width, length, and height of the one cube has to be greater than the other cube.
'''
