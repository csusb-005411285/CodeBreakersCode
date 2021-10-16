class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        return self.split(root, target)
    
    def split(self, node, target):
        if not node:
            return [None, None]
        if node.val <= target:
            root_tree_smaller_curr_node, root_tree_greater_curr_node = self.split(node.right, target)
            node.right = root_tree_smaller_curr_node
            return [node, root_tree_greater_curr_node] # 1.
        else:
            root_tree_smaller_curr_node, root_tree_greater_curr_node = self.split(node.left, target)
            node.left = root_tree_greater_curr_node
            return [root_tree_smaller_curr_node, node] # 1.
        
'''
1. Do not return node.left or node.right. The tree is being built at every step.
'''
