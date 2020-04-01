# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
		# init a queue
		queue = [self]
		# loop through the queue
		while queue:
			# pop element from the queue
			vertex = queue.pop(0)
			# if vertex not in array
			if vertex.name not in array:
				# then insert it in array
				array.append(vertex.name)
				# loop through the children
				for child in vertex.children:	
					# insert them in a queue
					queue.append(child)
		# return the array
		return array
        pass
	
    # 2nd attempt
    def breadthFirstSearch(self, array):
        # Write your code here.
		# init a deck
		queue = deque() # n
		# insert the current node in the deck
		queue.append(self)
		# loop through the deck
		while queue: # n
			# pop the node from the deck
			curr_node = queue.popleft()
			# if the node is in array
			if curr_node.name in array:
				continue
				# continue
				
			# insert the value in the array
			array.append(curr_node.name)
			# loop through the children
			for children in curr_node.children:
				# insert them in the deck
				queue.append(children)
				
		# return the deck
		return array 
