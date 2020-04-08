def boggleBoard(board, words):
    # Write your code here.
    # contruct a trie from the list of words
    words_trie = get_words_trie(words) #n
    # define a matrix to store visited vertices
    visited = [[False for col in rows] for rows in board] #n
    # define a dict to store the words found
    words_found = set() #n
    # write a function to explore neighbors to find the word in the list
    for row in range(len(board)): #n
        for col in range(len(board[row])): #n
            explore(words_trie, board, visited, words_found, [row, col]) #n
    return list(words_found)
    
def explore(words_trie, board, visited, words_found, vertex):
    i = vertex[0]
    j = vertex[1]
	
	if visited[i][j]:
		return

	if board[i][j] not in words_trie: 
		return

	visited[i][j] = True

	root_key = words_trie[board[i][j]]
	if '*' in root_key:
		words_found.add(root_key['*'])
	
	neighbors = get_neighbors(board, [i, j])
	for neighbor in neighbors:
		explore(root_key, board, visited, words_found, neighbor) #n
	visited[i][j] = False

def get_words_trie(words):
    trie = {}
    for word in words:
		curr_trie = trie
        for char in word:
            if char not in curr_trie:
				curr_trie[char] = {}
			curr_trie = curr_trie[char]	
        curr_trie['*'] = word
    return trie

def get_neighbors(board, vertex):
	neighbors = []
	row = vertex[0]
    col = vertex[1]
	if row > 0 and col > 0:
		neighbors.append([row - 1, col - 1])
	if row > 0:
		neighbors.append([row - 1, col])
	if row > 0  and col < len(board[0]) - 1:
		neighbors.append([row - 1, col + 1])
	if col > 0:
	  	neighbors.append([row, col - 1])
	if col < len(board[row]) - 1:
	  	neighbors.append([row, col + 1])
	if row < len(board) - 1 and col > 0:
	  	neighbors.append([row + 1, col - 1])
	if row < len(board) - 1:
	  	neighbors.append([row + 1, col])
	if row < len(board) - 1 and col < len(board[0]) - 1:
	  	neighbors.append([row + 1, col + 1])
	return neighbors
