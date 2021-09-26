class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # init vars
        # map to group points by their x or y coordinates
        points_map = defaultdict(list)
        # area
        area = float('inf')
        # last map
        last = {}
        # inital checks
        
        # process
        # count the number of x and y coordinates
        # store it in a set
        num_x_coord = set(x for x, y in points)
        # check if the x and y coordinates are unique
        num_y_coord = set(y for x, y in points)
        # the number of x an y coordinates should not be equal to the number of points
        if num_x_coord == len(points) or num_y_coord == len(points):
            return 0
        # group the points by x coordinates
        if num_x_coord > num_y_coord:
            for x, y in points:
                points_map[x].append(y)
        else:
            for x, y in points:
                points_map[y].append(x)
        # sort the dict
        sorted_points_map = sorted(points_map) # 1.
        # loop through the dict
        for x in sorted_points_map:
            # sort the values
            points_map[x].sort()
            # loop through the values
            for i in range(len(points_map[x])): # 2.
                # loop using anohter loop
                for j in range(i): # 2.
                    y1, y2 = points_map[x][j], points_map[x][i]
                    # check if the point exists
                    if (y1, y2) in last:  
                        # if it does
                        # get the min area
                        height = y2 - y1
                        width = x - last[y1, y2]
                        area = min(area, width * height)
                    # store points in a map
                    last[y1, y2] = x # 3.
        return area if area != float('inf') else 0
'''
1. sort the dict by x coordinates.
2. we get points in an increasing order. i.e x1 < x2 or y1 < y2. This is useful to calculate width or length of a side of a rectangle.
3. store the x coordinates common to the y coordinates or the other way around.
'''
