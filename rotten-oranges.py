class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    # init var to store row and column of the matrix
    row,col = len(grid), len(grid[0])
    # init a deck
    queue = collections.deque([])
    # init a var to store the number of fresh oranges
    num_fresh_oranges = 0
    # init a var to store the time
    time = 0
    # loop through the matrix
    for i in range(col):
      for j in range(row):
        if grid[i][j] == 1:
          # increment the numberof fresh oranges
          num_fresh_oranges += 1
        # if the orange is rotten
        if grid[i][j] == 2: 
          # store the row and column in the queue
          queue.append((i,j))
    
    # loop through the queue
    while queue:
      for _ in range(len(queue)):
        # pop the rotten orange from the queue
        i,j = queue.popleft()
        # check for the four adjacent cells
        for x, y in [(i + 1,j), (i - 1,j), (i,j + 1), (i,j - 1)]:
          # if the adjacent cell has a fresh orange
          if 0 <= x < col and 0 <= y < row and grid[x][y] == 1:
              # make it rotten
              grid[x][y] = 2
              # decrement the count of fresh oranges
              num_fresh_oranges -= 1
              # append the rotten orange to the queue
              queue.append((x,y))
      # increment the result after traversing one "row" of the "tree"
      time += 1
    # return res - 1 because the final iteration runs when all the oranges are rotten and there
    # are no fresh oranges left
    return max(0, time - 1) if num_fresh_oranges == 0 else -1
