# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        return self.dfs_helper(array, self, []) # O(v+e)
	
	def dfs_helper(self, array, vertex, visited = []):
		# if the vertex has no children
		if not vertex.children:	
			# add it to path
			array.append(vertex.name)
			# then return
			return
			
		# if the vertex has not been visited
		if vertex in visited:
			return
		
		# then add it to the visited list
		visited.append(vertex)
		# add it to the path
		array.append(vertex.name)
		
		# loop through the children of the vertex
		for children in vertex.children: # O(n)
			# call dfs recursively
			self.dfs_helper(array, children, visited) # O(n)
	
		# return path
		return array
