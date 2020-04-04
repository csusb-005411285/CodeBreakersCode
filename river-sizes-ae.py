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
