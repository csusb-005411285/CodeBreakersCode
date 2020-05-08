# tc: o(m+n), sc: o(1)
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
          return False
        
        visited1 = []
        visited2 = []
        self.leaf_similar_helper(root1, visited1)
        self.leaf_similar_helper(root2, visited2)
        return visited1 == visited2
    
    def leaf_similar_helper(self, root, visited = []):
        if not root.left and not root.right:
            visited.append(root.val)
            return
        
        if root.left:
            self.leaf_similar_helper(root.left, visited)

        if root.right:
            self.leaf_similar_helper(root.right, visited)

        return
