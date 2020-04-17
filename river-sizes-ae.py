from collections import deque

def riverSizes(matrix):
	# Write your code here.
	if len(matrix) == 0:
		return []
	if len(matrix) == 1 and len(matrix[0]) == 1:
		return [1] if matrix[0][0] == 1 else []
	
	# init a matrix to store visited vertices
	visited = [[False for cols in rows] for rows in matrix] #n
	# init a list to store sizes of rivers
	river_sizes = [] #1
	# init a deck
	stack = []#n
	# init a var to store current rivere size
	curr_river_size = 0
	
	# loop through the matrix
	for row in range(len(matrix)): #n
		for col in range(len(matrix[row])): #n
			# if it is land
			if matrix[row][col] == 0:	
				continue

			if visited[row][col]:
				continue

			curr_river_size = 0
			# insert the vertex in the stack
			stack = [[row, col]]
			# perform dfs
			# while stack is not empty
			while stack: #n
				# pop the element
				x, y = stack.pop()
				if visited[x][y]:
					continue
				
				visited[x][y] = True
				if matrix[x][y] == 0:
					continue

				# increment the size of river
				curr_river_size += 1		
				# get all neighbors
				# if the cell above is not visited
				if x > 1  and not visited[x - 1][y]:
					# then add it to the stack
					stack.append([x - 1, y])
				# else if the cell below is not visited
				if x < len(matrix) - 1 and not visited[x + 1][y]:
					# then add it to the stack
					stack.append([x + 1, y])
				# elseif the cell to the left is not visited
				if y > 0 and not visited[x][y - 1]:
					# then add it to the stack
					stack.append([x, y - 1])	
				if y < len(matrix[0]) - 1 and not visited[x][y + 1]:
					# then add it to the stack
					stack.append([x, y + 1])	
			# add to the size of the river to the result list
			if curr_river_size > 0:
				river_sizes.append(curr_river_size)
		
	# return the list
	return river_sizes		

# 2nd attempt
def riverSizes(matrix):
    # Write your code here.
    # init a matrix to store the visited vertices
    visited = [[False for col in rows] for rows in matrix]  # n
    # init a list to store the river sizes
    river_sizes = []  # n
    # init a deck
    stack = deque()  # n

    # loop through the matrix
    for row in range(len(matrix)):  # n
        for col in range(len(matrix[0])):  # n
            # init a var to store river sizes
            river_size = 0
            stack.append([row, col])
            # loop through the stack
            while stack:  # n
                # pop the element from the stack
                x, y = stack.pop()

                # if the element is visited
                if visited[x][y]:
                    continue

                # mark the element as visited
                visited[x][y] = True

                # if vert is 0 continue
                if matrix[x][y] == 0:
                    continue

                # then increment the river size
                river_size += 1

                # get the neighbors
                neighbors = get_neighbors(matrix, x, y)
                # insert the neighbors in the stack
                for neighbor in neighbors:
                    stack.append(neighbor)

                    if river_size > 0:
                        # add the river size to the list
                river_sizes.append(river_size)

    return river_sizes


def get_neighbors(matrix, x, y):
    neighbors = []
    if x > 0:
        neighbors.append([x - 1, y])
    if y > 0:
        neighbors.append([x, y - 1])
    if x < len(matrix) - 1:
        neighbors.append([x + 1, y])
    if y < len(matrix[0]) - 1:
        neighbors.append([x, y + 1])
    return neighbors

	# 3rd attempt. Recursive solution
def riverSizes(matrix):
  # Write your code here.
  visited = [[False for col in range(len(matrix[row]))] for row in range(len(matrix))]

  river_sizes = []

  for row in range(len(matrix)):
    curr_river_size = 0
    for col in range(len(matrix[row])):
      curr_river_size = dfs(matrix, [row, col], visited, 0)
      if curr_river_size: #
        river_sizes.append(curr_river_size) 
  return river_sizes

def dfs(matrix, vertex, visited, curr_river_size = 0):
  x, y = vertex
  if visited[x][y]:
    return 0;
  
  if matrix[x][y] != 1:
    return 0;

  visited[x][y] = True
  curr_river_size += 1

  for neighbor in get_neighbors(matrix, vertex):
    neigh_river_size = 0
    x_neigh, y_neigh = neighbor
    curr_river_size += dfs(matrix, [x_neigh, y_neigh], visited, 0)
  return curr_river_size

# alternate way to increment a counter
def dfs(matrix, vertex, visited, curr_river_size = 0):
  x, y = vertex
  if visited[x][y]:
    return curr_river_size
  
  if matrix[x][y] != 1:
    return curr_river_size

  visited[x][y] = True
  curr_river_size += 1

  for neighbor in get_neighbors(matrix, vertex):
    neigh_river_size = 0
    x_neigh, y_neigh = neighbor
    curr_river_size = dfs(matrix, [x_neigh, y_neigh], visited, curr_river_size)
  return curr_river_size

def get_neighbors(matrix, vertex):
  x, y = vertex
  neighbors = []
  if x > 0: # left
    neighbors.append([x - 1, y])
  if y > 0: # top
    neighbors.append([x, y - 1])
  if x < len(matrix) - 1: # right
    neighbors.append([x + 1, y])
  if y < len(matrix[x]) - 1: # bottom
    neighbors.append([x, y + 1])
  return neighbors
