class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # init vars
        # heap
        heap = []
        # visited
        visited = {}
        m = len(grid)
        n = len(grid[0])
        # inital checks
        # process
        # add the source to the heap
        # the heap should have a tuple of (cost, x, y)
        heappush(heap, (0, 0, 0))
        visited[(0, 0)] = 0
        # while the heap has elements, process
        while heap:
            # pop
            cost, x, y = heappop(heap)
            # if we reach the last cell
            if x == m - 1 and y == n - 1:
                return cost
            # get neighbors
            for n_x, n_y in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                new_cost = cost # 1.
                # if valid cell
                if 0 <= n_x < m and 0 <= n_y < n:
                    # if the val equals the position of the next cell
                    if (grid[x][y] == 1 and n_x == x and n_y == y + 1) or (grid[x][y] == 2 and n_x == x and n_y == y - 1) or (grid[x][y] == 3 and n_x == x + 1 and n_y == y) or (grid[x][y] == 4 and n_x == x - 1 and n_y == y):
                        # do not increment the cost
                        new_cost += 0
                    # if it does not
                    else:
                        # increment the cost
                        new_cost += 1
                    # if the cost to reach the neighbor is smaller than the current cost
                    # if the neighbor cell not visited
                    if (n_x, n_y) not in visited or visited[(n_x, n_y)] > new_cost:
                        # add to heap
                        heappush(heap, (new_cost, n_x, n_y))
                        # add to visited
                        visited[(n_x, n_y)] = new_cost
        return 0

'''
1. assign a new variable to store cost. Do not use the existing variable as it will be updated with values from previous iteration.
'''
