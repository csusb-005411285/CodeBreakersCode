class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    # init a var to store rows and cols
    rows = len(grid)
    cols = len(grid[0])
    # init a var to store the time
    time = 0
    # init a queue to store the rotten oranges
    rotten_oranges_queue = []
    # init a var to store the number of fresh oranges
    num_fresh_oranges = 0
    # loop through the grid to store the number of fresh oranges
    for row in range(rows):
      for col in range(cols):
        if grid[row][col] == 1:
          num_fresh_oranges += 1
        
        # store the rotten oranges in a queue
        if grid[row][col] == 2:
          rotten_oranges_queue.append([row, col])
    
    # perform BFS
    # loop until queue is not empty
    while rotten_oranges_queue: # O(n)
      # visit all elements of a queue
      size = len(rotten_oranges_queue)
      for _ in range(size): # O(n)
        # pop the first element
        i, j = rotten_oranges_queue.pop(0)
        # if any of the four neighbors are rotten
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]: # O(1)
          if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
            # mark the orange as rotten
            grid[x][y] = 2
            # enter it in the queue
            rotten_oranges_queue.append([x, y])
            # decrement the number of fresh oranges
            num_fresh_oranges -= 1
      # increment  the time
      time += 1
    
    # return the time or -1
    return max(0, time - 1) if num_fresh_oranges == 0 else -1
