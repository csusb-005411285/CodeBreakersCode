class Solution:
    def __init__(self):
        self.all_paths = []
        
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root.left and not root.right:
            return [str(root.val)]
        self._binary_tree_paths(root, [])
        return self.all_paths
    
    def _binary_tree_paths(self, node, path):
        if node and not node.left and not node.right:
            path.append(str(node.val))
            self.all_paths.append('->'.join(path))
            return
        if node.left:
            self._binary_tree_paths(node.left, path + [str(node.val)])
        if node.right:
            self._binary_tree_paths(node.right, path + [str(node.val)])
        return 
