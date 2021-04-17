class Solution:
    def __init__(self):
        self.inorder = []
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.get_inorder_traversal(root)
        return self.convert_list_tree(self.inorder)
    
    def get_inorder_traversal(self, node):
        if node and not node.left and not node.right:
            self.inorder.append(node.val)
            return
        if node.left:
            self.get_inorder_traversal(node.left)
        self.inorder.append(node.val)
        if node.right:
            self.get_inorder_traversal(node.right)
        return
    
    def convert_list_tree(self, node_list):
        if not node_list:
            return None
        left = 0
        right = len(node_list) - 1
        mid = left + (right - left)//2
        node = TreeNode(node_list[mid])
        node.left = self.convert_list_tree(node_list[:mid])
        node.right = self.convert_list_tree(node_list[mid + 1:])
        return node
