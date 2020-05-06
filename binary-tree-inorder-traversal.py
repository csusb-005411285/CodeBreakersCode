# tc: o(n), sc: o(n)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder_nodes = []
        if not root:
          return []
        
        if not root.left and not root.right:
          return [root.val]
        
        self.inorder_traversal_helper(root, inorder_nodes)        
        return inorder_nodes
    
    def inorder_traversal_helper(self, root, inorder_nodes): 
        if not root.left and not root.right:
            inorder_nodes.append(root.val)
            return 

        if root.left:
            self.inorder_traversal_helper(root.left, inorder_nodes)
        inorder_nodes.append(root.val)
        if root.right:
            self.inorder_traversal_helper(root.right, inorder_nodes)
        return 
