class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter_of_binary_tree_helper(root)
        return self.diameter
    
    def diameter_of_binary_tree_helper(self, node):
        if not node: return 0
        if not node.left and not node.right: return 1
        left_width = self.diameter_of_binary_tree_helper(node.left)
        right_width = self.diameter_of_binary_tree_helper(node.right)
        self.diameter = max(self.diameter, left_width + right_width)
        return max(left_width, right_width) + 1
