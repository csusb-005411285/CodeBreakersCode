class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    # if there is only one cell in the matrix
    if len(grid) == 1 and len(grid[0]) == 1: 
      # return -1
      if grid[0][0] == 1:
        return -1
      else:
        return 0
      
    # init a queue
    orange_queue = [] # O(n)
    # init a var to store the number of fresh oranges
    num_fresh_oranges = 0
    num_rotten_oranges = 0
    # init a var to store the minimum number of mins. elapsed.
    mins_elapsed = 0
    # init a var to store directions
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # init a var to store the visited cells
    visited = []
    for row in range(len(grid)): # O(n)
      for col in range(len(grid[0])): # O(n)
        if grid[row][col] == 1:
          num_fresh_oranges += 1
        
        if grid[row][col] == 2:
          num_rotten_oranges += 1
          orange_queue.append((row, col))
    
    if num_fresh_oranges == 0:
      return 0
    
    if num_rotten_oranges == 0:
      return -1
   
    # ahck alert
    orange_queue[:1]
    
    # perform BFS
    # while queue is not empty
    while orange_queue:
      size = len(orange_queue)
      for _ in range(size):
        # pop the first element
        orange = orange_queue.pop(0)
        # loop through the neighboring elements
        for x, y in directions: # O(1)
          neighbor_x = orange[0] + x
          neighbor_y = orange[1] + y
          # print('(' + str(neighbor_x) + ', ' + str(neighbor_y) + ') =>' + str(len(grid)) + ' => ' + str(len(grid[0])))
          # if the neighbor is fresh
          if 0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0]) and (neighbor_x, neighbor_y) not in visited:
            print(grid[neighbor_x][neighbor_y])
            if grid[neighbor_x][neighbor_y] == 1:
              # then make it rotten
              grid[neighbor_x][neighbor_y] = 2
              # insert it in the queue
              orange_queue.append((neighbor_x, neighbor_y))
              # decrement the fresh oranges
              num_fresh_oranges -= 1
              visited.append((neighbor_x, neighbor_y))
      # increment the var that stores the mins. elapsed
      mins_elapsed += 1
      
    # if no of fresh oranges is 0
    if num_fresh_oranges == 0:
      # then return mins. elapsed
      return mins_elapsed - 1
    # else
    else:
      # return -1
      return -1
