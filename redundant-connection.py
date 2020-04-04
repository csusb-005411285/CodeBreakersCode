class Solution:
  
  # init a constructor
  def __init__(self):
    self.parents = []
  
  def find_parent(self, x) -> int:
    # decrement the vertex by 1 so as to match the index
    if self.parents[x] == 0:
        return x
    self.parents[x] = self.find_parent(self.parents[x])
    return self.parents[x]

  
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # if there are no edges or one edge
    if len(edges) <= 1:  
        # return empty list
        return []
    
    # init a list to store the parents
    self.parents = [0 for _ in range(len(edges))]
    # for each edge
    for x, y in edges:
      # get the parent of each vertex
      parent_x = self.find_parent(x - 1)
      parent_y = self.find_parent(y - 1)
      # if the vertices have the same parent
      if parent_x == parent_y:
        # return the list of vertices
        return [x, y]
      self.parents[parent_x] = parent_y #
    return []
  
  # 2nd attempt
  def __init__(self):
    self.parents = []
  
  def find_vertex_with_no_children(self, vertex):
    # if the vertex does not have a child
    if self.parents[vertex] == 0:
      # then return the vertex, which means the index
      return vertex
    return self.find_vertex_with_no_children(self.parents[vertex])
    
  
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # if there are no edges or if there is only one edge
    if len(edges) <= 1:
      # then return the an empty list
      return []
    
    # init a list to store the parents
    self.parents = [0 for _ in range(len(edges))]
    
    # loop through edges
    for x, y in edges:
      # find the parent of each vertices
      root_x = self.find_vertex_with_no_children(x-1)
      root_y = self.find_vertex_with_no_children(y-1)
      # if the roots do not match
      if root_x != root_y:
        # then make one vertex the parent of the other
        self.parents[root_x] = root_y
      # else
      else:
        # return the vertices
        return [x, y]
    return []
        
   # 3rd attempt
   def __init(self):
    self.parents = []
  
  def find(self, vert: int) -> int:
    # if the vertex is a root
    if self.parents[vert] == 0:  
      # return the index
      return vert
    # go to the parent index
    return self.find(self.parents[vert])
  
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # if the edges are less than 1
    if len(edges) <= 1:
      # then return an empty list
      return []
    
    # init a list to store the parents
    self.parents = [0 for _ in range(len(edges))]
    # loop through each edge
    for edge in edges:
      x = edge[0] - 1
      y = edge[1] - 1
      # find the root of each vertex
      x_root = self.find(x)
      y_root = self.find(y)
      
      # if the vertices share the same root
      if x_root == y_root:
        # then return the vertices in a list
        return [edge[0], edge[1]]
      
      # make the first vertex the parent of the second vertex
      self.parents[x_root] = y_root    
    return []
    
  # 4th attempt
  def __init__(self):
    self.parents = [] # o(n)
  
  def find_root(self, vert):
    # if the vertex is root
    if self.parents[vert] == 0:
      # then return the index
      return vert
      
    # check the parent index
    return self.find_root(self.parents[vert])
  
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    self.parents = [0 for _ in range(len(edges))] #
    
    if len(edges) <= 1:
      return []
    
    # loop through the edges
    for edge in edges: # o(n)
      x = edge[0] - 1
      y = edge[1] - 1
      # for each edge, calculate the root of each vertex
      root_x = self.find_root(x)
      root_y = self.find_root(y)
      
      # if the roots are equal
      if root_x == root_y:
        # then return the list of vertices
        return [edge[0], edge[1]]
      
      # if the roots are not equal
        # then assign the root of x to be the parent of root of y
      self.parents[root_x] = root_y  
        
    
  # 5th attempt
  def __init__(self):
    self.parents = []
  
  def find_parent(self, vert)-> int:
    if self.parents[vert] == 0:
      return vert
    return self.find_parent(self.parents[vert]) 
  
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    self.parents = [0 for _ in range(len(edges))] #n
    
    # loop through the edges
    for x, y in edges: #n 
      # for each vertex find the parent
      x_parent = self.find_parent(x - 1)
      y_parent = self.find_parent(y - 1)
      # if they do not have a common parent
      if x_parent != y_parent:
        # then make the first vertex the parent of the second
        self.parents[x_parent] = y_parent
      else:
        # they are conncected
        # return the edge
        return [x, y]
      
