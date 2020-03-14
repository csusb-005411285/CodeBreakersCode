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
    
