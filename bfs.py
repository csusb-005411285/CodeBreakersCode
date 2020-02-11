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
