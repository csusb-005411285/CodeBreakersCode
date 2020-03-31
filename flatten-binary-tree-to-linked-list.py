class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
          return None
        
        self.dfs(root, [])
        
    def dfs(self, vert, visited = []):
      if vert in visited:
        return None
      
      visited.append(vert)
      if vert.left == None and vert.right == None:
        return vert
      
      left_vert = None
      right_vert = None 
      if vert.left:
        left_vert = self.dfs(vert.left, visited) # O(n)
      if vert.right:
        right_vert = self.dfs(vert.right, visited) # O(n)
        
      if left_vert:
        left_vert_tail = left_vert
        while left_vert_tail.right:
          left_vert_tail = left_vert_tail.right
        
        left_vert_tail.right = right_vert
        vert.right = left_vert
        vert.left = None 
      else:
        vert.right = right_vert
        vert.left = None 
      
        
      return vert
