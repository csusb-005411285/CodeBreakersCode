class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        self.get_inorder_traversal(root, inorder)
        return self.build_tree(inorder, 0, len(inorder) - 1)
    
    def get_inorder_traversal(self, node, inorder):
        stack = []
        while True:
            while node:
                stack.append(node)
                node = node.left
            if not stack:
                return inorder
            last_node = stack.pop()
            inorder.append(last_node.val)
            node = last_node.right
                
    def build_tree(self, inorder, left, right):
        if left > right:
            return None
        mid = left + (right - left)//2
        node_val = inorder[mid]
        node = TreeNode(node_val)
        node.left = self.build_tree(inorder, left, mid - 1)
        node.right = self.build_tree(inorder, mid + 1, right)
        return node
