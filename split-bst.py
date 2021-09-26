class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        return self.split_bst(root, target)
        
    def split_bst(self, node, target):
        if not node:
            return [None, None]
        if target >= node.val:
            root_smaller_nodes, root_greater_nodes = self.split_bst(node.right, target)
            node.right = root_smaller_nodes
            return [node, root_greater_nodes]
        else:
            root_smaller_nodes, root_greater_nodes = self.split_bst(node.left, target)
            node.left = root_greater_nodes
            return [root_smaller_nodes, node]
